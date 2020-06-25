import mido

def read_midi(filename:str) -> list:
    midiFile = mido.MidiFile(filename)
    notes_temp = dict()
    notes = []
    time = 0
    kk = set()
    for track in midiFile.tracks:
        time = 0
        for note in track:
            if note.type in ['note_on', 'note_off']:
                #TODO: get true time scale from midi file data
                time += note.time / 10000.0 * 3
            if note.type == 'note_on':
                notes_temp[note.note] = (time, note.velocity)
            elif note.type == 'note_off':
                try:
                    noteNumber = note.note
                    startTime, velocity = notes_temp.pop(noteNumber)
                    noteDuration = time - startTime
                    notes.append( (noteNumber, startTime, noteDuration, velocity) )
                except KeyError:
                    pass
    
    return notes