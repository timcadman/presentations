// Basemaps for FederatedQuery.vue. Each window must match the matplotlib call
// that draws it in ihen-26/build_maps.py — the component places nodes as
// percentages of these bounds, so the two cannot drift apart.
export const WINDOWS = {
  world: { file: '/world-base.png', lon: [-112, 95], lat: [-35, 60], size: [2070, 950] },
  europe: { file: '/europe-base.png', lon: [-11, 32], lat: [36, 58], size: [1200, 950] },
}

// Gazetteer: real coordinates, so a slide can just name a city.
export const CITIES = {
  Utrecht: [5.1214, 52.0907],
  Rotterdam: [4.4777, 51.9244],
  Groningen: [6.5665, 53.2194],
  Barcelona: [2.1686, 41.3874],
  Valencia: [-0.3763, 39.4699],
  Bristol: [-2.5879, 51.4545],
  Bradford: [-1.7594, 53.796],
  Copenhagen: [12.5683, 55.6761],
  Kaunas: [23.9036, 54.8985],
  Athens: [23.7275, 37.9838],
  Kampala: [32.5825, 0.3476],
  Nairobi: [36.8219, -1.2921],
  Accra: [-0.187, 5.6037],
  'Cape Town': [18.4241, -33.9249],
  Lima: [-77.0428, -12.0464],
  'New York': [-74.006, 40.7128],
  'São Paulo': [-46.6333, -23.5505],
  Bogotá: [-74.0721, 4.711],
  'New Delhi': [77.209, 28.6139],
  Bengaluru: [77.5946, 12.9716],
}
