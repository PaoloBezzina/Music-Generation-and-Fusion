let waitTimerGan = 430000

var genButtonGan = document.getElementById("slider-values");
var midAreaGan = document.getElementById("gan-file");

function displayMidiGan() {
  let midiTagGan = `<midi-player name="get-file-gan" src="static/ganOutputs/ganOutput.mid" sound-font></midi-player>`;
  midAreaGan.innerHTML = midiTagGan;
}

genButtonGan.onclick = function () {

  const progressElGan = document.getElementById("progressBarGan");
  progressElGan.style.display = 'block';

  let loadingTimeGan = setInterval(() => {
    progressElGan.value++;

    if (progressElGan.value >= progressElGan.max) {
      clearInterval(loadingTimeGan);
      console.log("Would replace");
    }
  }, 200);

  setTimeout(displayMidiGan, waitTimerGan);
}
