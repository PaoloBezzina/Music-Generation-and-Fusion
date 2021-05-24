# reproduced from: http://nickkellyresearch.com/python-script-transpose-midi-files-c-minor/

#converts all midi files in the current folder

import glob
import os
import music21

#converting everything into the key of C major or A minor

# major conversions
majors = dict([("A-", 4),("G#", 4),("A", 3),("A#", 2),("B-", 2),("B", 1),("C", 0),("C#", -1),("D-", -1),("D", -2),("D#", -3),("E-", -3),("E", -4),("F", -5),("F#", 6),("G-", 6),("G", 5)])
minors = dict([("G#", 1), ("A-", 1),("A", 0),("A#", -1),("B-", -1),("B", -2),("C", -3),("C#", -4),("D-", -4),("D", -5),("D#", 6),("E-", 6),("E", 5),("F", 4),("F#", 3),("G-", 3),("G", 2)])

print(glob.glob)

#os.chdir("./")
for file in glob.glob("classical-midis\*.mid"):

    # split_ = os.path.split(file)
    dir, filename = os.path.split(file)
    filename_comp = filename.split(",")

    composer_surname = filename_comp[0]
    composer_name = filename_comp[1]
    works_name = filename_comp[2]
    id = filename_comp[3]

    composers = ['Haydn']
    composerNames = [' Joseph']

    if composer_surname in composers:

        if composer_name in composerNames:
            print(composer_surname, " ", composer_name, " ", works_name, " ", id)
            
            score = music21.converter.parse(file)
            
            key = score.analyze('key')

            print("Original Key: " , key)

        #    print key.tonic.name, key.mode
            if key.mode == "major":
                halfSteps = majors[key.tonic.name]
                
            elif key.mode == "minor":
                halfSteps = minors[key.tonic.name]
            
            newscore = score.transpose(halfSteps)
            key = newscore.analyze('key')
            print(key.tonic.name, key.mode)
            newFileName = "transposed/" + filename
            print(newFileName)
            newscore.write('midi',newFileName)