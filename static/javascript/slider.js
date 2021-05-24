/* Slider 1 */
var val1 = 200;
var val2 = 0.5;
var val3 = 0.2;

var slider1 = document.getElementById("slider-1");
var outputSlider1 = document.getElementById("slider-1-value");
outputSlider1.innerHTML = slider1.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider1.oninput = function () {
    val1 = this.value;
    outputSlider1.innerHTML = this.value;
    document.querySelector(".value-1").value = this.value;
    updateValues();
}


/* Slider 2 */
var slider2 = document.getElementById("slider-2");
var outputSlider2 = document.getElementById("slider-2-value");
outputSlider2.innerHTML = slider2.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider2.oninput = function () {
    val2 = this.value;
    outputSlider2.innerHTML = this.value;
    document.querySelector(".value-2").value = this.value;
    updateValues();
}

/* Slider 3 */
var slider3 = document.getElementById("slider-3");
var outputSlider3 = document.getElementById("slider-3-value");
outputSlider3.innerHTML = slider3.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider3.oninput = function () {
    val3 = this.value;
    outputSlider3.innerHTML = this.value;
    document.querySelector(".value-3").value = this.value;
    updateValues();
}

/* Combine Values for return */
function updateValues(){
    var values = val1;
    values += ',';
    values += val2;
    values += ',';
    values += val3;
    document.getElementById("slider-values").value = values;
}