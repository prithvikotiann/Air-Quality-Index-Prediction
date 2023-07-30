// Get the sliders by their IDs
const coSlider = document.getElementById('co');
const ozoneSlider = document.getElementById('ozone');
const no2Slider = document.getElementById('no2');
const pmSlider = document.getElementById('pm');

// Get the spans that display the values
const coValueSpan = document.getElementById('coinput');
const ozoneValueSpan = document.getElementById('ozoneinput');
const no2ValueSpan = document.getElementById('noinput');
const pmValueSpan = document.getElementById('pminput');

// Event listeners for sliders' input changes
coSlider.addEventListener('input', function() {
  coValueSpan.textContent = coSlider.value;
});

ozoneSlider.addEventListener('input', function() {
  ozoneValueSpan.textContent = ozoneSlider.value;
});

no2Slider.addEventListener('input', function() {
  no2ValueSpan.textContent = no2Slider.value;
});

pmSlider.addEventListener('input', function() {
  pmValueSpan.textContent = pmSlider.value;
});
