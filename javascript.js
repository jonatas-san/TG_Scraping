function mostrarCardapio (id, id2){

    if (document.getElementById(id).style.display == 'none' && document.getElementById(id2).style.display == 'none'){
      document.getElementById(id).style.display = 'block';
      document.getElementById(id2).style.display = 'none';
    }
   else{
      document.getElementById(id).style.display = 'none';
      document.getElementById(id2).style.display = 'none'
    }
  }


function escodecheck(id){
  if (document.getElementById(id).style.display == 'none'){
      document.getElementById(id).style.display = 'block';
    }
   else{
      document.getElementById(id).style.display = 'none';
      document.getElementById(id2).style.display = 'none'
    }
  }

