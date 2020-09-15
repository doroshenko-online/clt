document.getElementById('setting-btn').onclick = function() {
  document.getElementById('settings-panel').classList.toggle('setting-active');
}

document.getElementById('btn-add').onclick = function() {
  document.getElementById('new-reminder__wrapper').classList.add('new-reminder__active');
}

document.getElementById('close-reminder-add').onclick = function() {
  document.getElementById('new-reminder__wrapper').classList.remove('new-reminder__active');
}
