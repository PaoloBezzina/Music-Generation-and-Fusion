//selecting all required elements
const dropArea = document.querySelector(".drag-area"),
    dragText = dropArea.querySelector("header"),
    button = dropArea.querySelector("button"),
    input = dropArea.querySelector("input");
let file; //this is a global variable and we'll use it inside multiple functions

button.onclick = () => {
    input.click(); //if user click on the button then the input also clicked
}

input.addEventListener("change", function () {
    //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = this.files[0];
    dropArea.classList.add("active");
    showFile(); //calling function
});


//If user Drag File Over DropArea
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault(); //preventing from default behaviour
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
});

//If user leave dragged File from DropArea
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload Midi File";
});

//If user drop File on DropArea
dropArea.addEventListener("drop", (event) => {
    event.preventDefault(); //preventing from default behaviour
    //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = event.dataTransfer.files[0];
    showFile(); //calling function
});


var form = document.getElementById('submit-button');
form.onclick = function () {
    alert("Button pressed!");
    form.style.display = 'none';
};

function toggle_display() {
    el = document.querySelector('.submit-button');
    if (el.style.display == 'none') {
        el.style.display = 'block'
    } else {
        el.style.display = 'none'
        document.getElementById("proc-msg").style.display = 'block';
    }
}

function showFile() {
    let fileType = file.type; //getting selected file type
    let validExtensions = ["audio/mid"]; //adding some valid image extensions in array
    if (validExtensions.includes(fileType)) { //if user selected file is an image file
        let fileReader = new FileReader(); //creating new FileReader object
        fileReader.onload = () => {
            let fileURL = fileReader.result; //passing user file source in fileURL variable
            // UNCOMMENT THIS BELOW LINE. I GOT AN ERROR WHILE UPLOADING THIS POST SO I COMMENTED IT
            let imgTag = `<midi-player name="get-file" src="${fileURL}" sound-font></midi-player>`; //creating an preview tag and passing user selected file source inside src attribute
            dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container

            let formTag = `<button onclick="toggle_display()" type="submit" class="submit-button" value='${fileURL}' name='processed-file'>Process</button>`
            document.querySelector(".file").innerHTML = formTag
        }
        fileReader.readAsDataURL(file);
    } else {
        alert("This is not a Midi File!");
        dropArea.classList.remove("active");
        dragText.textContent = "Drag & Drop to Upload File";
    }
}