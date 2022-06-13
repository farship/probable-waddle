function passport(){
    var password = prompt("Gordon, do you have your passport?");
    if (password !="Hello, Gordon!"){
        passport()
    }  
    else{
        alert("Another day, another dollar! Am I right?");
        startUp();
    }
}

function cacheElementVariables(){
    paperclipCounterElem = document.getElementById("paperclipCounter");
    lifetimePaperclipsCountElem = document.getElementById("lifetimePaperclipCounter");
    pricePerClipElem = document.getElementById("pricePerClip");
    marketDemandElem = document.getElementById("marketDemand");
    pricenumManualClipperElem = document.getElementById("priceManualClipper");
    numWireElem = document.getElementById("numWire");
    priceWireElem = document.getElementById("priceWire");
    buyWireElem = document.getElementById("buyWire");
    pricenumAutoClipperElem = document.getElementById("priceAutoClipper");
    numRPElem = document.getElementById("numRP");
    
    leftColumnElem = document.getElementById("leftColumn");
    middleColumnElem = document.getElementById("middleColumn");
    rightColumnElem = document.getElementById("rightColumn");
    
    devColumnElem = document.getElementById("devColumn");
    devAddClipsElem = document.getElementById("devAddClips");
}

//---ELEMENTS---//

var paperclipCounterElem;
var lifetimePaperclipsCountElem;
var pricePerClipElem;
var marketDemandElem;
var pricenumManualClipperElem;
var priceWireElem;
var numWireElem;
var buyWireElem;
var pricenumAutoClipperElem;
var leftColumnElem;
var middleColumnElem;
var rightColumnElem;
var numRPElem;




var devColumnElem;
var devAddClipsElem;
//---CHECKS---//

var projectsUnlockedCheck;

//---VALUES---//

var lifetimePaperclipsCount;
var currentPaperclipCount;
var pricePerClip;
var clipDemand;
var clipDemandPercent;
var numWire;
var priceWire;
var numManualClipper;
var priceManualClipper;
var numAutoClipper;
var priceAutoClipper;
var multiAutoClipper;
var numRP;
var RPGen;
var multiRPGen;
var numCP;
var CPGen;
var multiCPGen;



function startUp(){
    cacheElementVariables();
    currentPaperclipCount = 0;
    lifetimePaperclipsCount = 0;
    numWire = 1000;
    priceWire = 25;
    pricePerClip = 0.25;
    clipDemand = 76;
    clipDemandPercent = "76%";
    numManualClipper = 1;
    priceManualClipper = 100;
    numAutoClipper = 0;
    priceAutoClipper = 175;
    multiAutoClipper = 1;
    numRP = 0;
    RPGen = 1;
    multiRPGen = 1;
    numCP = 0;
    CPGen = 1;
    multiCPGen = 1;

    projectsUnlockedCheck = false;
    

    
    lifetimePaperclipsCount = lifetimePaperclipsCount + (numAutoClipper*multiAutoClipper);
    lifetimePaperclipsCountElem.innerHTML = "Total Paperclips: " + lifetimePaperclipsCount;
    currentPaperclipCount = currentPaperclipCount + (numAutoClipper*multiAutoClipper);
    paperclipCounterElem.innerHTML = "Paperclips: " + currentPaperclipCount;

    pricenumManualClipperElem.innerText = `+1 Manual Clipping (${priceManualClipper} Clips)`;

    numWireElem.innerText = `Wire: ${numWire}`;
    priceWireElem.innerText = `Cost: ${priceWire} Clips`;//ADD THE REMOVAL OF WIRE AND ADDING WHEN BUYING FUNCTION

    pricenumAutoClipperElem.innerText = `+1 Auto Clipper (${priceAutoClipper} Clips)`;
}

var interval1000 = setInterval(update1000, 1000);
function update1000(){
    autoClipper();
    

    lifetimePaperclipsCountElem.innerHTML = "Total Paperclips: " + lifetimePaperclipsCount;
    paperclipCounterElem.innerHTML = "Paperclips: " + currentPaperclipCount;

    numWireElem.innerText = `Wire: ${numWire}`;
    priceWireElem.innerText = `Cost: ${priceWire} Clips`;

    if (projectsUnlockedCheck == true) {
        addRP(RPGen*multiRPGen);
    }
}

var interval10000 = setInterval(update10000, 10000)
function update10000() {
    milestoneCheck()
    priceWire = Math.ceil((Math.random() * numWire)/40 + 5); //sets price of wire to be relative to the amount of wire avaliable

}




function manualClipper(){
    if (numWire >= numManualClipper) {
        addClips(numManualClipper);
    }
    else if (numWire > 0) {
        addClips(numWire);
    }
    
}

function buyManualClipper() {
    if (currentPaperclipCount >= priceManualClipper) {
        currentPaperclipCount -= priceManualClipper;
        numManualClipper += 1;
        priceManualClipper = Math.ceil(Math.pow(1.1, numManualClipper)+100);
        pricenumManualClipperElem.innerText = `+1 Manual Clipping (${priceManualClipper} Clips)`;
    }
}

function buyAutoClipper() {
    if (currentPaperclipCount >= priceAutoClipper) {
        currentPaperclipCount -= priceAutoClipper;
        numAutoClipper += 1;
        priceAutoClipper = Math.ceil(Math.pow(1.1, numAutoClipper)+175);
        pricenumAutoClipperElem.innerText = `+1 Auto Clipper (${priceAutoClipper} Clips)`;
    }
}

function autoClipper() {
    if (numWire >= (numAutoClipper*multiAutoClipper)) {
        addClips(numAutoClipper*multiAutoClipper);
    }
    else if (numWire > 0) {
        addClips(numWire);
    }
}

function buyWire() {
    if (currentPaperclipCount >= priceWire) {
        currentPaperclipCount-= priceWire;
        numWire += 1000;
    }
}

function addClips(number) {
    currentPaperclipCount += number;
    lifetimePaperclipsCount += number;
    numWire -= number;
}

function lowerPrice() {
    if (clipDemand < 100) {
        clipDemand += 1;
        pricePerClip = 100*(1.01 - 0.01*clipDemand);
        pricePerClip = (Math.floor(pricePerClip)/100)
        calcClipDemandPercent();
        marketDemandElem.innerText = (`${clipDemandPercent}%`);
        pricePerClipElem.innerText = pricePerClip;
    }
    
}
function calcClipDemandPercent() {
    clipDemandPercent = Math.ceil(100*(Math.sqrt(101-clipDemand)));//################FIX THIS
}

function higherPrice() {
    if (clipDemand > 1) {
        clipDemand -= 1;
        pricePerClip = 100*(1.01 - 0.01*clipDemand);
        pricePerClip = (Math.floor(pricePerClip)/100);//######skips sum
        calcClipDemandPercent();
        marketDemandElem.innerText = (`${clipDemandPercent}%`);
        pricePerClipElem.innerText = pricePerClip;
    }
}

function addRP(number) {
    numRP += number;
    numRPElem.innerText = `Research Points: ${numRP}`;
}

function addCP(number) {

}

function buyResearcher() {

}

function buyThinker() {
    
}





function milestoneCheck() {
    if (projectsUnlockedCheck == false){
        if (lifetimePaperclipsCount >= 1000){
            projectsUnlockedCheck = true;
            middleColumnElem.style.visibility = "visible";
        }
    }

}






function helloGordon(see) {
    devColumnElem.style.visibility = see;
}

function devAddClips(number) {
    currentPaperclipCount += number;
    lifetimePaperclipsCount += number;
}