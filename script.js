const maps = [
    {
        image: "Images/Anaheim_HE.png",
        caption: "Anaheim Candidate Sites Map",
        alt: "Published candidate sites map for Anaheim"
    },
    {
        image: "Images/Fullerton_HE.png",
        caption: "Fullerton Candidate Sites Map",
        alt: "Published candidate sites map for Fullerton"
    },
    {
        image: "Images/Irvine_HE.png",
        caption: "Irvine Candidate Sites Map",
        alt: "Published candidate sites map for Irvine"
    },
    {
        image: "Images/santa-ana-map.jpg",
        caption: "Santa Ana Candidate Sites Map",
        alt: "Published candidate sites map for Santa Ana"
    },
    {
        image: "Images/orange-map.jpg",
        caption: "Orange Candidate Sites Map",
        alt: "Published candidate sites map for Orange"
    }
];

let currentMap = 0;

function changeMap(direction) {
    currentMap += direction;

    if (currentMap >= maps.length) {
        currentMap = 0;
    }

    if (currentMap < 0) {
        currentMap = maps.length - 1;
    }

    const mapImage = document.getElementById("carousel-map");
    const mapCaption = document.getElementById("carousel-caption");

    mapImage.src = maps[currentMap].image;
    mapImage.alt = maps[currentMap].alt;
    mapCaption.textContent = maps[currentMap].caption;
}