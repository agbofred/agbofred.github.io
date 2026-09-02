const timeDisplay = document.querySelector('#studentTime');
const progressBar = document.querySelector('#studentProgress');
const params = new URLSearchParams(window.location.search);

let totalSeconds = Number(params.get('total')) || 300;
let remainingSeconds = Number(params.get('remaining')) || totalSeconds;
let timerId = null;

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
}

function stopTimer() {
  window.clearInterval(timerId);
  timerId = null;
}

function tick() {
  remainingSeconds = Math.max(0, remainingSeconds - 1);
  render();
  if (remainingSeconds === 0) stopTimer();
}

function applyState(state) {
  totalSeconds = Math.max(0, Number(state.totalSeconds) || 0);
  remainingSeconds = Math.max(0, Number(state.remainingSeconds) || 0);
  stopTimer();
  render();
  if (state.running && remainingSeconds > 0) timerId = window.setInterval(tick, 1000);
}

window.addEventListener('message', (event) => {
  if (event.data?.type === 'timer-state') applyState(event.data.state);
});

applyState({
  totalSeconds,
  remainingSeconds,
  running: params.get('running') === 'true'
});
