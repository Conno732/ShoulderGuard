canvas = document.createElement("canvas");
video = document.createElement("video");
canvas.setAttribute("width", 500);
canvas.setAttribute("height", 500);
video.setAttribute("width", 500);
video.setAttribute("height", 500);
if (document.getElementById("password") != null) {
  document.getElementById("password").addEventListener("click", () => {
    // window.open(
    //   "https://conno732.github.io/Alert-Page-For-ShoulderGuard/",
    //   "_blank"
    // );
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
            context.drawImage(video, 0, 0, 500, 500);
            var data = canvas.toDataURL("image/png");
            console.log(data);

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "https://shoulder-guarder.herokuapp.com/");
            xhr.onreadystatechange = function () {
              if (xhr.readyState === 4) {
                console.log(xhr.status);
                console.log(xhr.responseText);
              }
            };
            xhr.send(JSON.stringify({ picture: data }));
          })
          .then(() => {
            video.srcObject.getTracks()[0].stop();
          });
      });
  });
}
