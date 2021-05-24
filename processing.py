# pip install note-seq
# pip install -qU google-cloud magenta pyfluidsynth

import note_seq

import random
import string
from urllib import request as rq

# Setting Variables
SF2_PATH = "/content/Yamaha-C5-Salamander-JNv5.1.sf2"
SAMPLE_RATE = 16000
sampleLen = 30
returnFilename = "output.mid"

# Function definitions

# Convert note_seq to midi


def note_seq_to_midi(sequence):
    return note_seq.sequence_proto_to_midi_file(sequence, returnFilename)

# Convert midi file to note sequence from url


def getFileFromURL(url):

    with rq.urlopen(url) as response:
        data = response.read()

    header, encoded = url.split(",", 1)

    # tempFileName = str("{}.mid".format(encoded[-8:]))

    letters = string.ascii_lowercase
    tempFileName = (
        "static/midiFiles/{}.mid".format(''.join(random.choice(letters) for i in range(8))))

    # File qed jinqara u gie downloaded
    with open(tempFileName, "wb") as f:
        f.write(data)

    return tempFileName

# Convert midi file to note sequence


def getNoteSequence(path):
    return note_seq.midi_file_to_note_sequence(path)


# Handle sustain pedal in the seq.
def remSustain(seq):
    seq_nosus = note_seq.apply_sustain_control_changes(seq)
    return seq_nosus


# Trim to desired number of seconds. (Has to be without sustain)
def trimSeq(seq, max_seq_seconds):
    if seq.total_time > max_seq_seconds:
        print(" Shortening Midi file to %d seconds." % max_seq_seconds)
        seq = note_seq.extract_subsequence(seq, 0, max_seq_seconds)
        return seq


# Remove drums from seq if present.
def removeDrums(seq):
    if any(note.is_drum for note in seq.notes):
        print("File contains drums which will be removed.")
        notes = [note for note in seq.notes if not note.is_drum]
        del seq.notes[:]
        seq.notes.extend(notes)
    return seq


def getFileFromSeq(noteSeq, fName):
    note_seq.sequence_proto_to_midi_file(noteSeq, fName)
