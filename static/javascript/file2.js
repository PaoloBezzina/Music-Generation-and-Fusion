//selecting all required elements
const dropArea2 = document.querySelector(".drag-area2"),
    dragText2 = dropArea2.querySelector("header"),
    button2 = dropArea2.querySelector("button"),
    input2 = dropArea2.querySelector("input");
let file2; //this is a global variable and we'll use it inside multiple functions

button2.onclick = () => {
    input2.click(); //if user click on the button2 then the input2 also clicked
}

input2.addEventListener("change", function () {
    //getting user select file2 and [0] this means if user select multiple files2 then we'll select only the first one
    file2 = this.files[0];
    dropArea2.classList.add("active");
    showfile2(); //calling function
});


//If user Drag file2 Over dropArea2
dropArea2.addEventListener("dragover", (event) => {
    event.preventDefault(); //preventing from default behaviour
    dropArea2.classList.add("active");
    dragText2.textContent = "Release to Upload file";
});

//If user leave dragged file2 from dropArea2
dropArea2.addEventListener("dragleave", () => {
    dropArea2.classList.remove("active");
    dragText2.textContent = "Drag & Drop to Upload Midi File";
});

//If user drop file2 on dropArea2
dropArea2.addEventListener("drop", (event) => {
    event.preventDefault(); //preventing from default behaviour
    //getting user select file2 and [0] this means if user select multiple files2 then we'll select only the first one
    file2 = event.dataTransfer.files[0];
    showfile2(); //calling function
});

function toggle_display_2() {
    el = document.querySelector('.submit-button-2');
    if (el.style.display == 'none') {
        el.style.display = 'block'
    } else {
        el.style.display = 'none'
        document.getElementById("proc-msg-2").style.display = 'block';
    }
}

function showfile2() {
    let file2Type = file2.type; //getting selected file2 type
    let validExtensions = ["audio/mid"]; //adding some valid image extensions in array
    if (validExtensions.includes(file2Type)) { //if user selected file2 is an image file2
        let fileReader2 = new FileReader(); //creating new file2Reader object
        fileReader2.onload = () => {
            let file2URL = fileReader2.result; //passing user file2 source in file2URL variable
            // UNCOMMENT THIS BELOW LINE. I GOT AN ERROR WHILE UPLOADING THIS POST SO I COMMENTED IT
            let imgTag = `<midi-player src="${file2URL}" sound-font></midi-player>`; //creating an preview tag and passing user selected file2 source inside src attribute
            dropArea2.innerHTML = imgTag; //adding that created img tag inside dropArea2 container

            let formTag = `<button onclick="toggle_display_2()" type="submit" class="submit-button-2" value='${file2URL}' name='processed-file-2'>Process</button>`
            document.querySelector(".file2").innerHTML = formTag
        }
        fileReader2.readAsDataURL(file2);
    } else {
        alert("This is not a Midi file!");
        dropArea2.classList.remove("active");
        dragText2.textContent = "Drag & Drop to Upload file2";
    }
}
