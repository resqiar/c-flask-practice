function countHypotenuse() {
  const inputA = document.querySelector("#input-a").value;
  const inputB = document.querySelector("#input-b").value;
  if (!inputA || !inputB) return resetUI();

  axios
    .post("/hypotenuse", {
      inputA: inputA,
      inputB: inputB,
    })
    .then((response) => {
      bindUI(response);
    })
    .catch((err) => {
      console.log(err);
    });
}

function bindUI(response) {
  const bigTextUI = document.querySelector("#hypotenuse-h1");
  const textUI = document.querySelector("#result-p");
  bigTextUI.innerHTML = response.data.result.toFixed(2);
  textUI.innerHTML = `C (Hypotenuse) = ${Math.round(response.data.result)}`;
}

function resetUI() {
  const bigTextUI = document.querySelector("#hypotenuse-h1");
  bigTextUI.innerHTML = "";
}

function hitEnter(event) {
  if (event.key === "Enter") {
    countHypotenuse();
  }
}
