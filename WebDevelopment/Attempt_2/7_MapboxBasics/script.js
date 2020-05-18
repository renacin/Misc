//
// Name:                                            Renacin Matadeen
// Date:                                               05/18/2020
// Title                                            MapBox Basics
//
// ----------------------------------------------------------------------------------------------------------------------

mapboxgl.accessToken = "pk.eyJ1IjoicmVuYWNpbiIsImEiOiJja2E4bjltazUwMHZnMnlqcGlxaWIwM204In0.iHbzIg1r383eOg505sRukg"
const map = new mapboxgl.Map({
    container: "MainMap",
    style: "mapbox://styles/renacin/ckaciuja04m4q1is2ujckpkeh",
    center: [-79.378048,  43.684352],
    pitch: 0, // pitch in degrees
    bearing: -16.20, //bearing in degrees
    zoom: 11.11,

})

// disable map zoom when using scroll
map.scrollZoom.disable();
map.pan.disable();
