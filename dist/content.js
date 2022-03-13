let popup = document.createElement("div");
popup.id = "popup-overlay-Original";
popup.style.position = "fixed";
popup.style.display = "none";
popup.style.width = "100%";
popup.style.height = "100%";
popup.style.top = "0";
popup.style.bottom = "0";
popup.style.left = "0";
popup.style.right = "0";
popup.style.backgroundColor = "rgba(220,20,60,.9)";
popup.style.zIndex = "2";
popup.style.cursor = "pointer";
popup.style.justifyContent = "center";
popup.style.alignItems = "center";
document.body.appendChild(popup);

popup.innerHTML = `<div style="width: 30%; height: 70%; background-color: white; display:flex; 
algin-items:center; padding:15px; flex-direction:column; gap:20px">
<h1 style="font-weight: bolder; text-align: center; margin-bottom:32px"> Alert! </h1>
<p style=" text-align: center;">We noticed someone was looking at your screen as you were typing in sensitive info.</p>
<p style=" bolder; text-align: center;">This popup is to prevent any shoulder surfers from stealing your passwords/information.</p>
<p style=" bolder; text-align: center;">Please refrain from entering sensitive info in front of others.</p>
</div>`;

popup.addEventListener("click", () => {
  popup.style.display = "none";
});

canvas = document.createElement("canvas");
video = document.createElement("video");
canvas.setAttribute("width", 500);
canvas.setAttribute("height", 500);
video.setAttribute("width", 500);
video.setAttribute("height", 500);
if (document.getElementById("password") != null) {
  document.getElementById("password").addEventListener("click", () => {
    var context = canvas.getContext("2d");
    canvas.width = 500;
    canvas.height = 500;
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: false })
      .then(function (stream) {
        video.srcObject = stream;
        video
          .play()
          .then(() => {
            checkCamera(context);
          })
          .then(() => {
            video.srcObject.getTracks()[0].stop();
          });
      });
  });
}

function alertPopupOn() {
  popup.style.display = "flex";
}

function checkCamera(context) {
  context.drawImage(video, 0, 0, 500, 500);
  var data = canvas.toDataURL("image/png");
  console.log(" ");

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "https://shoulder-guarder.herokuapp.com/");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4) {
      responseD = xhr.responseText;
      if (responseD.includes("false")) {
        console.log("No");
      } else {
        console.log("Yes");
        alertPopupOn();
      }
    }
  };
  xhr.send(JSON.stringify({ picture: data }));
}
