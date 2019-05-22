//used in index.html to automatically submit when Buzzcard is scanned
function auto_submit() {
  let x = document.getElementById("gtid").value;
  if (x.length == 9) {
    document.getElementById("myForm").submit();
  }

}


//used in ta.html to confirm clearing the queue
function clearConfirm(event) {
  if (!confirm("You are about to clear the ENTIRE queue, are you sure you want to do this?")) {
    event.preventDefault();
  }
}
//used in ta.html to confirm signing out
function signOutConfirm(event) {
  if (!confirm("You are about to Sign-Out of FyeFo, are you sure you want to do this?")) {
    event.preventDefault();
  }
}

//used in both index.html and ta.html to fetch the queue and current TAs from the server-side
function on_load() {
  fetch("/queue")
    .then(response => response.json())
    .then(myJson => load_queue(myJson["queue"], myJson["tas"]));
}

//called after 10s have elapsed on ta.html to ensure TA doesn't accidentily not stay signed in
function timeOut() {
  document.getElementById("exit").click();
}


//used by both index.html and ta.html
//contains all the logic to display the queue and TAs on duty
function load_queue(queue, tas) {


  let block_num = 0;
  //outer div id=queue"
  let container = document.getElementById("queue");
  for (var i = 0; i < queue.length; i++) {
    block_num = Math.floor(i / 5) + 1;
    let queue_element = document.getElementById("block" +  block_num.toString());
    let num = (i + 1).toString() + ". ";
    let para = document.createElement("p");
    let node = document.createTextNode(num + queue[i]);
    para.appendChild(node);
    queue_element.appendChild(para);
    //gives us the number for css id
    container.appendChild(queue_element);


  }

  // TA displaying
  let tas_element = document.getElementById("tas");
  //dictionary (JS obj containing TA's pictures)
  var picdict = {"Jakob Brian Johnson":"jakob.png",
                  "Damian William Henry":"damian.png"}
  for (var i = 0; i < tas.length; i++) {
    
    let container = document.createElement("div");
    container.id = "ta" + (i + 1).toString();
    container.className = "ta-name";
    var para = document.createElement("p");
    var node = document.createTextNode(tas[i]);
    para.appendChild(node);

    var DOM_img = document.createElement("img");
    DOM_img.src = "static/"+ picdict[tas[i]]
    DOM_img.height = 150;
    DOM_img.width = 90;

    var br = document.createElement("br");
    container.appendChild(br);
    
    container.appendChild(DOM_img);
    container.appendChild(para);

    tas_element.appendChild(container);
  }



}
function validate_disappear() {
  let flag = document.getElementById("invalid") || document.getElementById("not_on_roster");
  if (flag) {
    setTimeout(() => flag.style.display = 'none', 5000);
  }
}
 

