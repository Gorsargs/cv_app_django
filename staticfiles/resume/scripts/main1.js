
function fieldnamevalidator(classname){
  const elements = document.getElementsByClassName(classname);
  console.log(elements)
}

function addSkill () {
    const elements = document.getElementsByClassName('yui-u skills');
    let tag = document. createElement("div");
    tag.className = 'talent';
    tag.innerHTML = `
      <input type="button" value="x" class = "myButton" onclick="remove('yui-u skills',this)">
      <input name="skillname" class="skillname" type="text" placeholder="Your Skill Name">
      <textarea name="skilltext" class="skilltext" name="" id="" cols="22" rows="10"
        placeholder="Skill Description"></textarea>
      
    `;
    elements[0].appendChild(tag);
}


function addTechnical() {
    const arrforpick = ['Adobe Illustrator','css','html','Adobe Photoshop','Js','Python','WordPress'];
    let rand = Math.random();
    rand *= arrforpick.length;
    rand = Math.floor(rand);
    console.log(rand);
    const elements = document.getElementsByClassName('yui-u Technical');
    let tag = document.createElement("div");
    tag.className = 'talent';
    tag.innerHTML = `
      <input type="button" class="myButton" id="minusbutton" value="x" onclick="remove('yui-u Technical',this)"></input>  
      <input  name="technical" type="text" placeholder = "skill e.g ${arrforpick[rand]}"></input>
    `;
    elements[0].appendChild(tag);
}



function addJob() {
  const elements = document.getElementsByClassName('yui-u Experience');
  let tag = document.createElement("div");
  tag.className = 'job';
  tag.innerHTML = `
      <h2><input name="companyname" type="text" placeholder="Company"></h2>
      <h3><input name="position" type="text" placeholder="Position"></h3>
      <h4><input name="data-field" type="text" placeholder="e.g Jul 2020 - Feb 2022"></h4>
      <textarea name="aboutwork" cols="60" rows="4" style="resize: none;" placeholder = "About Work"></textarea>
      <input class="myMinusButton" type="button" value="x" onclick="remove('yui-u Experience',this)">

  `;
  elements[0].appendChild(tag);
}
function addlinkfield(){
    const elements = document.getElementsByClassName('yui-u contact')
    let tag = document.createElement("h3")
    tag.innerHTML = `
        <input name="additionalinfo" type="text" placeholder = "additional contact info..."></input>
        <input class= "myMinusButton" type="button" value = "x" onclick = "remove('yui-u contact',this)"></input>
    `
    elements[0].appendChild(tag)
}

function addEducation() {
    const elements = document.getElementsByClassName('yui-u education');
    let tag = document.createElement("div");
    tag.className = 'job education';
    tag.innerHTML = `
        <h2><input name="education" type="text" name="Educationplace" placeholder="Education place"></h2>
        <h4><input name="education-data" type="text" placeholder="e.g Jul 2020 - Feb 2022"></h4>
        <h3><input name="educationfield" type="text" placeholder="Education field"></h3>
        <h2><input name="gpa" type="text" placeholder="1-4 gpa"></h2>
        <input class="myMinusButton" type="button" value="x" onclick="remove('yui-u education',this)">
    `;
    elements[0].appendChild(tag);
}


function remove(classname,input) {
  document.getElementsByClassName(classname)[0].removeChild(input.parentNode);
}


