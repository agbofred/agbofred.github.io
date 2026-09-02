const timeDisplay = document.querySelector('#timeDisplay');
const progressBar = document.querySelector('#progressBar');
const status = document.querySelector('#timerHeading');
const startButton = document.querySelector('#startButton');
const resetButton = document.querySelector('#resetButton');
const setButton = document.querySelector('#setButton');
const minutesInput = document.querySelector('#minutesInput');
const secondsInput = document.querySelector('#secondsInput');
const fullscreenButton = document.querySelector('#fullscreenButton');
const studentViewButton = document.querySelector('#studentViewButton');
const presetButtons = document.querySelectorAll('[data-minutes]');

let totalSeconds = 300;
let remainingSeconds = totalSeconds;
let timerId = null;
let studentWindow = null;

function broadcastState() {
  const state = { totalSeconds, remainingSeconds, running: Boolean(timerId) };
  if (studentWindow && !studentWindow.closed) studentWindow.postMessage({ type: 'timer-state', state }, '*');
}

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60).toString().padStart(2, '0');
  const remainder = (seconds % 60).toString().padStart(2, '0');
  return `${minutes}:${remainder}`;
}

function render() {
  timeDisplay.textContent = formatTime(remainingSeconds);
  document.title = `${formatTime(remainingSeconds)} | Classroom Timer`;
  const progress = totalSeconds === 0 ? 0 : remainingSeconds / totalSeconds;
  progressBar.style.transform = `scaleX(${progress})`;
  timeDisplay.classList.toggle('finished', remainingSeconds === 0);
  progressBar.classList.toggle('finished', remainingSeconds === 0);
  broadcastState();
}

function stopTimer() {
  window.clearInterval(timerId);
  timerId = null;
}

function finishTimer() {
  stopTimer();
  status.textContent = 'Time is up';
  startButton.textContent = 'Start again';
  playBell();
}

function tick() {
  remainingSeconds -= 1;
  render();
  if (remainingSeconds <= 0) finishTimer();
}

function toggleTimer() {
  if (timerId) {
    stopTimer();
    status.textContent = 'Paused';
    startButton.textContent = 'Resume';
    broadcastState();
    return;
  }

  if (remainingSeconds === 0) remainingSeconds = totalSeconds;
  status.textContent = 'Students are working';
  startButton.textContent = 'Pause';
  render();
  timerId = window.setInterval(tick, 1000);
  broadcastState();
}

function setDuration(minutes, seconds = 0) {
  stopTimer();
  totalSeconds = Math.max(0, (minutes * 60) + seconds);
  remainingSeconds = totalSeconds;
  minutesInput.value = minutes;
  secondsInput.value = seconds;
  status.textContent = totalSeconds ? 'Ready when you are' : 'Set a duration to begin';
  startButton.textContent = 'Start timer';
  render();
}

function readDuration() {
  const minutes = Math.min(99, Math.max(0, Number.parseInt(minutesInput.value, 10) || 0));
  const seconds = Math.min(59, Math.max(0, Number.parseInt(secondsInput.value, 10) || 0));
  setDuration(minutes, seconds);
}

function resetTimer() {
  stopTimer();
  remainingSeconds = totalSeconds;
  status.textContent = 'Ready when you are';
  startButton.textContent = 'Start timer';
  render();
}

function openStudentView() {
  const params = new URLSearchParams({
    total: totalSeconds,
    remaining: remainingSeconds,
    running: Boolean(timerId)
  });
  studentWindow = window.open(`student.html?${params}`, 'classroomTimerStudent', 'popup=yes,width=420,height=180');
  if (studentWindow) {
    studentWindow.focus();
    studentViewButton.textContent = 'Student view open';
  }
}

function playBell() {
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  const gain = audioContext.createGain();
  oscillator.frequency.value = 660;
  gain.gain.setValueAtTime(0.18, audioContext.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.8);
  oscillator.connect(gain).connect(audioContext.destination);
  oscillator.start();
  oscillator.stop(audioContext.currentTime + 0.8);
}

startButton.addEventListener('click', toggleTimer);
resetButton.addEventListener('click', resetTimer);
studentViewButton.addEventListener('click', openStudentView);
setButton.addEventListener('click', readDuration);
minutesInput.addEventListener('keydown', (event) => { if (event.key === 'Enter') readDuration(); });
secondsInput.addEventListener('keydown', (event) => { if (event.key === 'Enter') readDuration(); });
presetButtons.forEach((button) => button.addEventListener('click', () => setDuration(Number(button.dataset.minutes))));

document.addEventListener('keydown', (event) => {
  if (event.code === 'Space' && document.activeElement.tagName !== 'INPUT') {
    event.preventDefault();
    toggleTimer();
  }
});

fullscreenButton.addEventListener('click', async () => {
  if (!document.fullscreenElement) await document.documentElement.requestFullscreen();
  else await document.exitFullscreen();
});

document.addEventListener('fullscreenchange', () => {
  const isFullscreen = Boolean(document.fullscreenElement);
  fullscreenButton.textContent = isFullscreen ? '×' : '⛶';
  fullscreenButton.title = isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen';
  fullscreenButton.setAttribute('aria-label', fullscreenButton.title);
});

render();
