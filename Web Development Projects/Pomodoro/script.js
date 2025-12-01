let mapa;       
let geocoder;

function initMap() {
  const coordenadasIniciais = { lat: -23.5505, lng: -46.6333 };

  mapa = new google.maps.Map(document.getElementById("mapa"), {
    center: coordenadasIniciais,
    zoom: 12,
  });

  geocoder = new google.maps.Geocoder();

  console.log("Mapa e Geocoder inicializados.");
}

function buscarLocalizacao() {
  const endereco = document.getElementById("endereco-input").value;

  if (!endereco) {
    alert("Digite um endereço válido.");
    return;
  }

  geocoder.geocode({ address: endereco }, (results, status) => {
    if (status === "OK" && results[0]) {
      const localizacao = results[0].geometry.location;

      mapa.setCenter(localizacao);
      mapa.setZoom(15);

      new google.maps.Marker({
        map: mapa,
        position: localizacao,
        title: results[0].formatted_address,
      });

      console.log("Local encontrado:", results[0].formatted_address);
    } else {
      alert("Erro ao buscar endereço. Status: " + status);
      console.error("Erro no Geocoding:", status);
    }
  });
}
