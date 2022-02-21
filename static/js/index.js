function convertScore() {
  // input value
  const scoreValue = document.querySelector("#input").value;
  if (!scoreValue) return resetUI();

  axios
    .post("/score", {
      score: scoreValue,
    })
    .then((response) => {
      bindUI(response);
    })
    .catch((err) => {
      console.log(err);
    });
}

function bindUI(response) {
  const bigTextUI = document.querySelector("#result-h1");
  const smallTextUI = document.querySelector("#result-p");

  bigTextUI.innerHTML = response.data.letter;
  smallTextUI.innerHTML = response.data.text;
}

function resetUI() {
  const bigTextUI = document.querySelector("#result-h1");
  const smallTextUI = document.querySelector("#result-p");

  bigTextUI.innerHTML = "";
  smallTextUI.innerHTML = "";
}

function hitEnter(event) {
  if (event.key === "Enter") {
    convertScore();
  }
}
