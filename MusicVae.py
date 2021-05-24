from flask import Flask, flash
import note_seq
from magenta.models.music_vae.trained_model import TrainedModel

from magenta.models import music_vae

import random


def interpolate(model, start_seq, end_seq, num_steps, max_length=32,
                assert_same_length=True, temperature=0.5,
                individual_duration=32):

    # Interpolates between a start and end sequence.
    note_sequences = model.interpolate(
        start_seq, end_seq, num_steps=num_steps, length=max_length,
        temperature=temperature,
        assert_same_length=assert_same_length)

    # concatenates sequences , from start to end as a single track
    interp_seq = note_seq.sequences_lib.concatenate_sequences(
        note_sequences, [individual_duration] * len(note_sequences))

    note_seq.plot_sequence(interp_seq)
    return interp_seq if num_steps > 2 else note_sequences[num_steps // 2]


def musicFusion(midi1, midi2):

    hierdec_mel_16bar_config = music_vae.configs.CONFIG_MAP['hierdec-mel_16bar']
    mel_16_bar = TrainedModel(hierdec_mel_16bar_config, batch_size=4,
                              checkpoint_dir_or_path='checkpoints/hierdec-mel_16bar.tar')

    # hardcoded midi files samples

    mel_input_seqs = [note_seq.midi_file_to_note_sequence(
        midi1), note_seq.midi_file_to_note_sequence(midi2)]
    extracted_16_mels = []

    firstSample = True
    for ns in mel_input_seqs:
        extracted_16_mels.extend(
            hierdec_mel_16bar_config.data_converter.from_tensors(
                hierdec_mel_16bar_config.data_converter.to_tensors(ns)[1]))

        if firstSample:
            number_of_samples = len(extracted_16_mels)
            firstSample = False

    """ 
    # Creating extracted melody files (to check)
    for i, ns in enumerate(extracted_16_mels):
        note_seq.note_sequence_to_midi_file(ns, str(i)+'.mid')
        print("Melody", i)
    """

    if len(extracted_16_mels) == 0:
        flash(u'No melodies extracted from both Midi Files!', 'error')
        return "No melodies extracted from both Midi Files!"

    if number_of_samples == 0:
        flash(u'No melodies extracted from the first Midi File!', 'error')
        return "No melodies extracted from the first Midi File!"

    if len(extracted_16_mels) == number_of_samples:
        flash(u'No melodies extracted from the second Midi File!', 'error')
        return "No melodies extracted from the second Midi File!"

    start_mel = extracted_16_mels[random.randint(0, number_of_samples-1)]
    end_mel = extracted_16_mels[random.randint(
        number_of_samples, len(extracted_16_mels)-1)]

    index_melody1 = random.randint(0,number_of_samples-1)
    index_melody2 = random.randint(number_of_samples, len(extracted_16_mels)-1)

    start_mel = extracted_16_mels[index_melody1]

    end_mel = extracted_16_mels[index_melody2]

    print("Chosen Melody: "+str(index_melody1))
    print("Chosen Melody: "+str(index_melody2))

    temperature = 0.7

    interpolation = interpolate(
        mel_16_bar, start_mel, end_mel, num_steps=4, temperature=temperature)

    note_seq.note_sequence_to_midi_file(
        interpolation, 'static/midiFiles/vaeFusion.mid')
