/*
 * File: AdventureScript.js
 * ------------------------
 * This file implements a slow-motion script.
 */

"use strict";

class AdventureScript {

    constructor(id, script) {
        this._target = document.getElementById(id);
        this._script = script;
        this._lx = 0;
        this._cx = 0;
        this._inputFlag = false;
        this._target.innerHTML = "";
    }

    start() {
        let delay = (this._inputFlag) ? INPUT_TIME_STEP : OUTPUT_TIME_STEP;
        this._timer = setInterval(step, delay);
        let obj = this;
        let n = obj._script.length;
    
        function step() {
            while (obj._lx < n && obj._cx === obj._script[obj._lx].length) {
                obj._lx++;
                obj._cx = 0;
                if (obj._inputFlag) {
                    obj._inputFlag = false;
                    clearInterval(obj._timer);
                    obj._timer = setInterval(step, OUTPUT_TIME_STEP);
                }
                obj._target.innerHTML += "<br />";
            }
            if (obj._lx === n) {
                clearInterval(obj._timer);
            } else {
                let ch = obj._script[obj._lx][obj._cx++];
                if (ch === ">") ch = "&gt;";
                if (ch === "@") ch = "&thinsp;";
                if (ch === " ") ch = "&nbsp;";
                if (obj._inputFlag) {
                    let text = obj._target.innerHTML;
                    let len = text.length;
                    let head = text.substring(0, len - 7);
                    obj._target.innerHTML = head + ch + "</span>";
                } else {
                    obj._target.innerHTML += ch;
                }
                if (ch === "&gt;" || ch === "&thinsp;") {
                    clearInterval(obj._timer);
                    if (ch === "&gt;") {
                        obj._target.innerHTML +=
                            "<span style='color:blue;'></span>";
                        obj._inputFlag = true;
                    }
                }
            }
        }

    }

}

const OUTPUT_TIME_STEP = 30;
const INPUT_TIME_STEP = 100;

const CROWTHER_SCRIPT = [
    "Welcome to ADVENTURE!!  Would you like instructions?",
    "",
    "> YES",
    "",
    "Somewhere nearby is Colossal Cave, where others have found fortunes",
    "in treasure and gold, though it is rumored that some who enter are",
    "never seen again.  Magic is said to work in the cave.  I will be your",
    "eyes and hands.  Direct me with natural English commands; I don't",
    "understand all of the English language, but I do a pretty good job.",
    "(Should you get stuck, type \"HELP\" for some general hints.)",
    "-----",
    "You are standing at the end of a road before a small brick building.",
    "Around you is a forest.  A small stream flows out of the building and",
    "down a gully to the south.  The road runs up a small hill to the west.",
    "",
    "> IN",
    "",
    "You are inside a building, a well house for a large spring. . . ."
];

const SLOW_MACHINE_SCRIPT = [
    "You are in the Hall of the Mountain King, with passages off",
    "in most directions, some of which appear to be newly constructed.",
    "A huge green fierce snake bars the way!",
    "",
    "> RELEASE BIRD",
    "",
    "The little bird attacks the green snake, and in an astounding flurry",
    "drives the snake away.",
    "",
    "@",
    "",
    "You are in a secret canyon which exits to the north and east.",
    "A huge fierce green dragon bars the way!",
    "The dragon is sprawled out on a persian rug!!",
    "",
    "> RELEASE BIRD",
    "",
    "The little bird attacks the green dragon, and in an astounding flurry",
    "gets burnt to a cinder.  The ashes blow away."
];

const MILESTONE1_SCRIPT = [
    "You are standing at the end of a road before a small brick",
    "building.  A small stream flows out of the building and",
    "down a gully to the south.  The road runs up a small hill",
    "to the west.",
    "> WEST",
    "You are at the end of a road at the top of a small hill.",
    "You can see a small building in the valley to the east.",
    "You are inside a building, a well house for a large spring. . . .",
    "> EAST",
    "You are standing at the end of a road before a small brick",
    "building.  A small stream flows out of the building and",
    "down a gully to the south.  The road runs up a small hill",
    "to the west."
];

const MILESTONE2_SCRIPT = [
    "You are standing at the end of a road before a small brick",
    "building.  A small stream flows out of the building and",
    "down a gully to the south.  A road runs up a small hill",
    "to the west.",
    "> WEST",
    "You are at the end of a road at the top of a small hill.",
    "You can see a small building in the valley to the east.",
    "> EAST",
    "Outside building."
];

const MILESTONE3_SCRIPT = [
    "You are standing at the end of a road before a small brick",
    "building.  A small stream flows out of the building and",
    "down a gully to the south.  A road runs up a small hill",
    "to the west.",
    "> WEST",
    "You are at the end of a road at the top of a small hill.",
    "You can see a small building in the valley to the east.",
    "> EAST",
    "Outside building.",
    "> LOOK",
    "You are standing at the end of a road before a small brick",
    "building. A small stream flows out of the building and",
    "down a gully to the south. A road runs up a small hill",
    "to the west.",
    "> QUIT"
];

const MILESTONE4_SCRIPT = [
    "Outside building.",
    "> IN",
    "You are inside a building, a well house for a large spring.",
    "The exit door is to the south. There is another room to",
    "the north, but the door is barred by a shimmering curtain.",
    "There is a set of keys here.",
    ">"
];

const MILESTONE5_SCRIPT = [
    "You are inside a building, a well house for a large spring.",
    "The exit door is to the south.  There is another room to",
    "the north, but the door is barred by a shimmering curtain.",
    "There is a set of keys here.",
    "> TAKE KEYS",
    "Taken.",
    "> TAKE GOLD",
    "I don't see that here.",
    "> INVENTORY",
    "You are carrying:",
    "  a bottle of water",
    "  a set of keys",
    "> DROP WATER",
    "Dropped.",
    "> DROP KEYS",
    "Dropped.",
    "> INVENTORY",
    "You are empty-handed.",
    ">"
];

const MILESTONE6_SCRIPT = [
    "You are standing at the end of a road before a small brick",
    "building.  A small stream flows out of the building and",
    "down a gully to the south.  A road runs up a small hill",
    "to the west.",
    "> I",
    "You are carrying:",
    "  a bottle of water",
    "> DROP BOTTLE",
    "Dropped.",
    "> W",
    "You are at the end of a road at the top of a small hill.",
    "You can see a small building in the valley to the east.",
    "> D",
    "Outside building.",
    "There is a bottle of water here.",
    ">"
];

const MILESTONE7_SCRIPT = [
    "You are in a 20-foot depression floored with bare dirt.",
    "Set into the dirt is a strong steel grate mounted in",
    "concrete.  A dry streambed leads into the depression from",
    "the north.",
    "> INVENTORY",
    "You are carrying:",
    "  a bottle of water",
    "  a set of keys",
    "> DOWN",
    "You are in a small chamber beneath a 3x3 steel grate to",
    "the surface.  A low crawl over cobbles leads inward to",
    "the west.",
    "There is a brightly shining brass lamp here.",
    ">"
]; 
 
const MILESTONE8_SCRIPT = [
    "You are in a 20-foot depression floored with bare dirt.",
    "Set into the dirt is a strong steel grate mounted in",
    "concrete.  A dry streambed leads into the depression from",
    "the north.",
    "> INVENTORY",
    "You are carrying:",
    "  a bottle of water",
    "> DOWN",
    "The grate is locked and you don't have any keys.",
    "Outside grate.",
    ">"
] ;

function CrowtherScriptDemo() {
    let scripter = new AdventureScript("CrowtherConsole",
                                       CROWTHER_SCRIPT);
    CodeTrace.registerFragmentEvent("CrowtherMark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("CrowtherMark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("CrowtherMark2",
        function() {
            scripter.start();
        });
}

function SlowMachineDemo() {
    let scripter = new AdventureScript("SlowMachineConsole",
                                       SLOW_MACHINE_SCRIPT);
    CodeTrace.registerFragmentEvent("SlowMark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("SlowMark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("SlowMark2",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("SlowMark3",
        function() {
            scripter.start();
        });
}

function Milestone1Demo() {
    let scripter = new AdventureScript("Milestone1Console",
                                       MILESTONE1_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone1Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone1Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone1Mark2",
        function() {
            scripter.start();
        });
}

function Milestone2Demo() {
    let scripter = new AdventureScript("Milestone2Console",
                                       MILESTONE2_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone2Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone2Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone2Mark2",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone2Mark3",
        function() {
            scripter.start();
        });
}

function Milestone3Demo() {
    let scripter = new AdventureScript("Milestone3Console",
                                       MILESTONE3_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone3Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone3Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone3Mark2",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone3Mark3",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone3Mark4",
        function() {
            scripter.start();
        });
}

function Milestone4Demo() {
    let scripter = new AdventureScript("Milestone4Console",
                                       MILESTONE4_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone4Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone4Mark1",
        function() {
            scripter.start();
        });
}

function Milestone5Demo() {
    let scripter = new AdventureScript("Milestone5Console",
                                       MILESTONE5_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone5Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark2",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark3",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark4",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark5",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone5Mark6",
        function() {
            scripter.start();
        });
}

function Milestone6Demo() {
    let scripter = new AdventureScript("Milestone6Console",
                                       MILESTONE6_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone6Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone6Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone6Mark2",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone6Mark3",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone6Mark4",
        function() {
            scripter.start();
        });
}

function Milestone7Demo() {
    let scripter = new AdventureScript("Milestone7Console",
                                       MILESTONE7_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone7Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone7Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone7Mark2",
        function() {
            scripter.start();
        });
}

function Milestone8Demo() {
    let scripter = new AdventureScript("Milestone8Console",
                                       MILESTONE8_SCRIPT);
    CodeTrace.registerFragmentEvent("Milestone8Mark0",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone8Mark1",
        function() {
            scripter.start();
        });
    CodeTrace.registerFragmentEvent("Milestone8Mark2",
        function() {
            scripter.start();
        });
}
