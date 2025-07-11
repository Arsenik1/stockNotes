const { spawnSync } = require('child_process');
const { ipcRenderer } = require('electron');
const path = require('path');

let mode = 'undefined';
let defaultDate = '';

function updateDisplay() {
  document.getElementById('modeDisplay').textContent = mode;
  document.getElementById('dateDisplay').textContent = defaultDate || 'none';
}

function runBackend(args) {
  const script = path.resolve(__dirname, '..', 'backend.py');
  const result = spawnSync('python', [script, ...args], { encoding: 'utf-8' });
  if (result.error) {
    alert(result.error.message);
    return '';
  }
  if (result.stderr) {
    console.error(result.stderr);
  }
  return result.stdout.trim();
}

document.getElementById('setDate').addEventListener('click', () => {
  const choice = prompt("Choose date option:\n1. Today's date\n2. Custom date");
  if (choice === '1') {
    const now = new Date();
    const dd = String(now.getDate()).padStart(2, '0');
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const yyyy = now.getFullYear();
    defaultDate = `${dd}-${mm}-${yyyy}`;
  } else if (choice === '2') {
    const custom = prompt('Enter the default date (DD-MM-YYYY):');
    if (custom) {
      defaultDate = custom;
    }
  }
  updateDisplay();
});

document.getElementById('switchMode').addEventListener('click', () => {
  mode = mode === 'long' ? 'short' : 'long';
  alert('Switched to ' + mode + ' mode');
  updateDisplay();
});

document.getElementById('listCompanies').addEventListener('click', () => {
  const out = runBackend(['list']);
  document.getElementById('output').textContent = out;
});

document.getElementById('addStock').addEventListener('click', () => {
  const code = prompt('Enter the stock code:');
  if (!code) return;
  runBackend(['add-stock', code]);
  alert('Stock code added.');
});

document.getElementById('addNote').addEventListener('click', () => {
  if (mode === 'undefined') {
    alert('Please set the mode first.');
    return;
  }
  const code = prompt('Enter the stock code:');
  if (!code) return;
  const note = prompt('Enter your note:');
  if (!note) return;
  const args = ['add-note', code, note];
  if (defaultDate) args.push('--date', defaultDate);
  if (mode) args.push('--mode', mode);
  runBackend(args);
  alert('Note added.');
});

document.getElementById('readNotes').addEventListener('click', () => {
  const code = prompt('Enter the stock code:');
  if (!code) return;
  const out = runBackend(['read', code]);
  document.getElementById('output').textContent = out;
});

document.getElementById('readAll').addEventListener('click', () => {
  const file = prompt('Enter output filename:');
  if (!file) return;
  runBackend(['dump', file]);
  alert('All notes saved to ' + file);
});

document.getElementById('exitApp').addEventListener('click', () => {
  ipcRenderer.send('quit');
});

updateDisplay();
