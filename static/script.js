const urlParams = new URLSearchParams(window.location.search);
const audioSrc = decodeURIComponent(urlParams.get('audio') || '');
const thumb = decodeURIComponent(urlParams.get('thumb') || '');
const title = decodeURIComponent(urlParams.get('title') || 'Unknown Title');

const audio = document.getElementById('audio');
const seek = document.getElementById('seek');
const currentTime = document.getElementById('current');
const totalTime = document.getElementById('total');

document.getElementById('thumb').src = thumb;
document.getElementById('title').innerText = title;
document.getElementById('artist').innerText = 'Now Playing';

audio.src = audioSrc;
audio.loop = false;
audio.autoplay = true;

// Autoplay fallback
function tryAutoPlay() {
  audio.play().catch(err => {
    console.warn("Autoplay blocked:", err);
  });
}

audio.addEventListener('loadedmetadata', () => {
  totalTime.innerText = formatTime(audio.duration);
  tryAutoPlay();
});

audio.addEventListener('timeupdate', () => {
  seek.value = (audio.currentTime / audio.duration) * 100;
  currentTime.innerText = formatTime(audio.currentTime);
});

seek.addEventListener('input', () => {
  audio.currentTime = (seek.value / 100) * audio.duration;
});

function togglePlay() {
  if (audio.paused) {
    audio.play();
  } else {
    audio.pause();
  }
}
function stopAudio() {
  audio.pause();
  audio.currentTime = 0;
}
function endPlayer() {
  stopAudio();
  alert("Player ended. Please close the tab.");
}
function rewind() {
  audio.currentTime = Math.max(0, audio.currentTime - 10);
}
function forward() {
  audio.currentTime = Math.min(audio.duration, audio.currentTime + 10);
}
function backward() {
  audio.currentTime = 0;
}
function formatTime(sec) {
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return `${m}:${s < 10 ? '0' + s : s}`;
}
document.addEventListener("visibilitychange", () => {
  if (document.visibilityState === "visible") {
    tryAutoPlay();
  }
});
audio.addEventListener("canplay", tryAutoPlay);