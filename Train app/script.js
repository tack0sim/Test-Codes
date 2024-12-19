// work in progress...

const result = document.getElementById("result");
const activityLog = document.getElementById("decision");
const wakeUp = document.getElementsByName("wakeUp");
const breakfast = document.getElementsByName("breakfast");
const submitData = document.getElementById("submit");
const ticker = document.querySelector(".ticker");

submitData.textContent = "Submit";

let train = "10:30";
ticker.textContent = `Wake up! Your train leaves at ${train}!`;

// submit decision:
submitData.addEventListener("click", checkData);

// logic:
function checkData() {
    if (wakeUp === "" || breakfast === "") {
        result.textContent = "Give an answer to all questions!";
    } else if (wakeUp > 9){
        result.textContent = "You overslept! You will not make the train!";
        wakeUp.disabled = true;
        breakfast.disabled = true;
        //gameOver();
    } else if (breakfast > 10) {
        result.textContent = "You took too long to finish breakfast. You will not make the train!";
        wakeUp.disabled = true;
        breakfast.disabled = true;
        //gameOver();
    } else {
        result.textContent = "You will make the train! Yaay!";
        wakeUp.disable = true;
        breakfast.disabled = true;
        //gameOver();
    }
}

// game over function:
function gameOver(){
    btn = document.createElement("button");
    btn.textContent = "Game Over! Reset";
    btn.addEventListener("click", reset());
}

function reset() {
    wakeUp.value = "";
    breakfast.value = "";
    wakeUp.disabled = false;
    breakfast.disabled = false;
}
