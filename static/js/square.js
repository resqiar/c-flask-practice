function countSquareRoot() {
  // input value
  const inputValue = document.querySelector("#input").value;
  if (!inputValue) return resetUI();

  axios
    .post("/squareroot", {
      number: inputValue,
    })
    .then((response) => {
      bindUI(response);
    })
    .catch((err) => {
      console.log(err);
    });
}

function bindUI(response) {
  const textUI = document.querySelector("#square-h1");
  textUI.innerHTML = response.data.result.toFixed(2);
}

function resetUI() {
  const textUI = document.querySelector("#square-h1");
  textUI.innerHTML = "";
}

function hitEnter(event) {
  if (event.key === "Enter") {
    countSquareRoot();
  }
}
