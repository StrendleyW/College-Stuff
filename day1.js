const { Readline } = require("readline/promises");

const readline = require("readline").createInterface({
    input : process.stdin,
    output : process.stdout
    });

function randomChoices() {
    const choices = ["gunting", "batu", "kertas"];
    const randomNumber = Math.floor(Math.random() * choices.length);
    return choices[randomNumber];
}

console.clear();

readline.question("Pilihan Pemain : ", (result) => {
    const playerChoice = result;
    const computerChoice = randomChoices();

    console.log("Pilihan Computer : "  + computerChoice);
    
    if (playerChoice == "gunting" && computerChoice == "kertas"){
        console.log("Pemain Menang");
    } else if ((playerChoice == "batu" && computerChoice == "gunting")){
        console.log("Pemain Menang");
    } else if ((playerChoice == "kertas" && computerChoice == "batu")){
        console.log("Pemain Menang");
    } else if ((playerChoice == computerChoice)){
        console.log("seri");
    } else {
        console.log("Komputer Menang");
    }

    readline.close();
});






/*const usia = 41;

if(usia<20){
    console.log("Minor, I win")
} else if (usia>=20 && usia<40){
    console.log("Kamu Sudah Cukup Umur")
} else if (usia>=40){
    console.log("Kamu Sudah Terlalu Cukup Umur")
}


/*const mahasiswaA = "Doni";
const mahasiswaB = "Joki";
const mahasiswaC = "Andika";

const mahasiwa = ["Doni", "Joki", "Andika"]

console.log(mahasiwa[1]);

/*function greet(name) {
    console.log('Halo GDSC!');
    return "Halo Namaku " + name;
}



/*greet()
const response = greet("Strendley")

const umur = 20;

console.log(playerChoice);
console.log(response)*/