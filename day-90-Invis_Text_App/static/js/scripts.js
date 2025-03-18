let timer;

function handleKeyUp() {
    window.clearTimeout(timer); // prevents multiple timers, used to clear the message even if you started typing again

    let countdown = 5; // 5s timer
    const status = document.getElementById("status");
    const typer = document.getElementById("typer");

    //initial countdown
    status.innerHTML = `Start typing! Text clears in ${countdown} seconds...`;

    //countdown timer
    timer = setInterval(() => {
        countdown--;

        if (countdown > 0) {
            status.innerHTML = `Start typing! Text clears in ${countdown} seconds...`;
        } else {

            typer.value = "";        //resets text area when countdown finished
            status.innerHTML = "Text cleared!";
            clearInterval(timer); // Stop countdown
        }
    }, 1000); //runs every second
}

//event listener attached to the type box
document.addEventListener("DOMContentLoaded", function () {
    const typer = document.getElementById("typer");
    typer.addEventListener("keyup", handleKeyUp);
});
