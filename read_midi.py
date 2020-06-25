import mido

def read_midi(filename:str) -> list:
    midiFile = mido.MidiFile(filename)
    notes_temp = dict()
    notes = []
    time = 0
    for track in midiFile.tracks:
        for note in track:
            if note.type in ['note_on', 'note_off']:
                time += note.time / 10000.0
            if note.type == 'note_on':
                notes_temp[note.note] = (time, note.velocity)
            elif note.type == 'note_off':
                noteNumber = note.note
                startTime, velocity = notes_temp.pop(noteNumber)
                noteDuration = time - startTime
                notes.append( (noteNumber, startTime) )
                # notes.append( (noteNumber, startTime, noteDuration, velocity) ) # not fully implemented yet
    
    return notes