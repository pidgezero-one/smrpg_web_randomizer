const framerate = 60.0988138974405;
const notes_ = [
  { note: "Fa", alt: "F4", val: 0 },
  { note: "So", alt: "G4", val: 1 },
  { note: "La", alt: "A5", val: 2 },
  { note: "Ti", alt: "B5", val: 3 },
  { note: "Do", alt: "C5", val: 4 },
  { note: "Re", alt: "D5", val: 5 },
  { note: "Mi", alt: "E5", val: 6 }
];
const notes = notes_.slice(0).reverse();

const NoteBox = (props) => {
  const updateNumberField = (e) => {
    const v = e.target.value;
    props.adjustDelay(props.column, v);
  };

  if (!props.note) {
    return (
      <div
        className="notebox"
        onClick={() => props.moveNote(props.column, props.row)}
      />
    );
  } else {
    return (
      <div className="notebox">
	  <input
          type="number"
          step="1"
          min="0"
          max="255"
          defaultValue={props.note.pause}
          onChange={updateNumberField}
		  disabled={props.column === 7}
	  />
      </div>
    );
  }
};

const Column = (props) => {
  return (
    <div className="column">
      {notes.map((n) => {
        if (n.val === props.note.val) {
          return (
            <NoteBox
              note={props.note}
              column={props.index}
              row={n.val}
              adjustDelay={props.adjustDelay}
              moveNote={props.moveNote}
            />
          );
        } else {
          return (
            <NoteBox
              column={props.index}
              row={n.val}
              moveNote={props.moveNote}
              adjustDelay={props.adjustDelay}
            />
          );
        }
      })}
      {props.showRemover && (
        <div
          className="removeNote"
          onClick={() => props.moveNote(props.index, undefined)}
        >
          <div>×</div>
        </div>
      )}
    </div>
  );
};

const LabelColumn = () => {
  return (
    <div className="labelColumn">
      {notes.map((n) => (
        <div className="labelBox">
          <div>
            ({n.val}) {n.note} {n.alt}
          </div>
        </div>
      ))}
    </div>
  );
};

const playFa= [];
const playSo= [];
const playLa= [];
const playTi= [];
const playDo= [];
const playRe= [];
const playMi= [];

Array(8).fill(null).forEach((_, index) => {
	const noteFa = document.getElementById("fa_" + index);
	playFa.push(noteFa.play.bind(noteFa));
	const noteSo = document.getElementById("so_" + index);
	playSo.push(noteSo.play.bind(noteSo));
	const noteLa = document.getElementById("la_" + index);
	playLa.push(noteLa.play.bind(noteLa));
	const noteTi = document.getElementById("ti_" + index);
	playTi.push(noteTi.play.bind(noteTi));
	const noteDo = document.getElementById("do_" + index);
	playDo.push(noteDo.play.bind(noteDo));
	const noteRe = document.getElementById("re_" + index);
	playRe.push(noteRe.play.bind(noteRe));
	const noteMi = document.getElementById("mi_" + index);
	playMi.push(noteMi.play.bind(noteMi));
});

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      notes: [
        { val: 1, pause: 35 },
        { val: 2, pause: 35 },
        { val: 6, pause: 35 },
        { val: 5, pause: 35 },
        { val: 4, pause: 35 },
        { val: 5, pause: 35 },
        { val: 4, pause: 35 },
        { val: 5, pause: 0 }
      ]
    };

    this.moveNote = this.moveNote.bind(this);
    this.adjustDelay = this.adjustDelay.bind(this);
    this.playSong = this.playSong.bind(this);
  }

  componentDidMount() {}
  componentDidUpdate() {}

  moveNote(column, row) {
    //don't allow re-inserting a note at the end if it leave a space between other notes. apply notes in order
    if (
      this.state.notes[column].val === undefined &&
      column > 0 &&
      this.state.notes[column - 1].val === undefined
    ) {
      return;
    }
	
	if (row === 0) {
		playFa[column]()
	}
	else if (row === 1) {
		playSo[column]()
	}
	else if (row === 2) {
		playLa[column]()
	}
	else if (row === 3) {
		playTi[column]()
	}
	else if (row === 4) {
		playDo[column]()
	}
	else if (row === 5) {
		playRe[column]()
	}
	else if (row === 6) {
		playMi[column]()
	}

    let n = [...this.state.notes];
    n[column].val = row;
    this.setState({ notes: n });
    this.forceUpdate();
  }

  adjustDelay(column, delay) {
    this.setState((currentState) => {
      let n = [...currentState.notes];
      n[column].pause = delay;
      return { notes: n };
    });
    this.forceUpdate();
  }

  playSong() {
	const blank = () => {
		return;
	}
	const playback = this.state.notes.map((n, index) => {
		if (n.val === 0) {
			return playFa[index]
		}
		else if (n.val === 1) {
			return playSo[index]
		}
		else if (n.val === 2) {
			return playLa[index]
		}
		else if (n.val === 3) {
			return playTi[index]
		}
		else if (n.val === 4) {
			return playDo[index]
		}
		else if (n.val === 5) {
			return playRe[index]
		}
		else if (n.val === 6) {
			return playMi[index]
		}
		else {
			return blank
		}
	});
	
	const getMilliseconds = (frames) => frames / framerate * 1000
	
	delay(playback[0], 200)
		.delay(playback[1], getMilliseconds(this.state.notes[0].pause))
		.delay(playback[2], getMilliseconds(this.state.notes[1].pause))
		.delay(playback[3], getMilliseconds(this.state.notes[2].pause))
		.delay(playback[4], getMilliseconds(this.state.notes[3].pause))
		.delay(playback[5], getMilliseconds(this.state.notes[4].pause))
		.delay(playback[6], getMilliseconds(this.state.notes[5].pause))
		.delay(playback[7], getMilliseconds(this.state.notes[6].pause))
	
	
  }

  render() {
    const song = [...this.state.notes];
    return (
      <div>
        <div className="upper">
          <div className="scoreContainer">
            <div className="score">
              <LabelColumn />
              {Array(8)
                .fill(null)
                .map((_, index) => {
                  const n = index >= song.length ? undefined : song[index];
                  const shouldShowRemover =
                    n.val !== undefined &&
                    (index === song.length - 1 ||
                      song[index + 1].val === undefined);
                  return (
                    <Column
                      note={n}
                      index={index}
                      moveNote={this.moveNote}
                      adjustDelay={this.adjustDelay}
                      showRemover={shouldShowRemover}
                    />
                  );
                })}
            </div>
            <button className="playback" onClick={this.playSong}>Play</button>
          </div>
          <div className="yourSong">
            If you want to submit this to SMRPG Randomizer,
            <br />
            copy-paste the following into the <a target="_blank" href="https://docs.google.com/forms/d/18h1eYKoxX0oUxVqYBhR2OcrNuhkHHYA0J322foNtKUQ">submission form</a>:
            <br />
            <br />
            {song.map((n) => {
              if (n.val !== undefined) {
                const syllable = notes.find((s) => s.val === n.val);
                return (
                  <div>
                    {syllable.note}-{n.val}-{n.pause}
                  </div>
                );
              } else {
                return undefined;
              }
            })}
          </div>
        </div>
        <div className="instructions">
          <h1>Tadpole Pond Composer</h1>
          Notes are represented by black boxes.
          <br />
          In each column, click on any square to move the note up or down.
          <br />
          The number in the box is how many frames you want the game to pause
          after that note plays.
          <br />
          (In the original game, it is always 35 frames between notes.)
          <br />
          Click on the red X to remove the last note.
          <br />
          (There cannot be notes missing between other notes, use the frame
          counter instead.)
        </div>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));

function delay(fn, t) {
    // private instance variables
    var queue = [], self, timer;
    
    function schedule(fn, t) {
        timer = setTimeout(function() {
            timer = null;
            fn();
            if (queue.length) {
                var item = queue.shift();
                schedule(item.fn, item.t);
            }
        }, t);            
    }
    self = {
        delay: function(fn, t) {
            // if already queuing things or running a timer, 
            //   then just add to the queue
        	  if (queue.length || timer) {
                queue.push({fn: fn, t: t});
            } else {
                // no queue or timer yet, so schedule the timer
                schedule(fn, t);
            }
            return self;
        },
        cancel: function() {
            clearTimeout(timer);
            queue = [];
            return self;
        }
    };
    return self.delay(fn, t);
}
