function pesquisar_endereco(){

    options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cep: document.getElementById('inputCep').value })
    }

    fetch(url, options)
      .then(function (response){
        return response.json();
      })
      .then(function (data){
        document.getElementById('inputLogradouro').value = data['logradouro']
        document.getElementById('inputBairro').value = data['bairro']
        document.getElementById('inputCidade').value = data['cidade']
        document.getElementById('inputEstado').value = data['estado']
      });
  }

function vtnc(){
   return console.log("VAI SE FUDER PROGRAMA FDP!!")
}