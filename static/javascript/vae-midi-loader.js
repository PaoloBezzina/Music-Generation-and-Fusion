let waitLoadingVae = 21000

var genButtonVae = document.getElementById("vae-fusion");
var midAreaVae = document.getElementById("vae-file");

function displayMidiVae() {
  let midiTagVae = `<midi-player name="get-file-vae" src="static/midiFiles/vaeFusion.mid" sound-font></midi-player>`;
  midAreaVae.innerHTML = midiTagVae;
}

genButtonVae.onclick = function () {
  const progressElVae = document.getElementById("progressBarVae");
  progressElVae.style.display = 'block';
  
  let loadingTimeVae = setInterval(() => {
    progressElVae.value++;

    if (progressElVae.value >= progressElVae.max) {
      clearInterval(loadingTimeVae);
      console.log("Would replace");
    }
  }, 200);

  setTimeout(displayMidiVae, waitLoadingVae);
}
