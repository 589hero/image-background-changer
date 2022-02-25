function formSend() {
  const formData = new FormData();
  const orgImage = document.getElementById('org-img-input').files[0];
  const bgImage = document.getElementById('bg-img-input').files[0];

  if(orgImage == null){
      alert("Input the Original Image");
      return;
  }
  else if(bgImage == null){
      alert("Input the Background Image");
        return;
    }

  formData.append("orgImage", orgImage);
	formData.append("bgImage", bgImage);
	
  fetch(
    '/change-bg',
    {
      method: 'POST',
      body: formData,
    }
  )
  .then(response => {
    if (response.status == 200){
      return response
    }
    else{
      throw Error("Error occurs while changing background.")
    }
  })
  .then(response => response.blob())
  .then(blob => URL.createObjectURL(blob))
  .then(imageURL => {
    document.getElementById("result-img").setAttribute("src", imageURL);
  })
  .catch(e =>{
  })
}

function setThumbnail(event, id){
  const uploaderId = id + '-input';
  const uploadImagePath = document.getElementById(uploaderId).value;

  if(uploadImagePath.length == 0){
    document.getElementById(id).setAttribute("src", '../static/images/thumbnail-1.jpeg');
    document.getElementById('result-img').setAttribute("src", '../static/images/thumbnail-1.jpeg');
  } else{
    const reader = new FileReader();
  
    reader.onload = function(event){
      document.getElementById(id).setAttribute("src", event.target.result);
    };
  
    reader.readAsDataURL(event.target.files[0]);
  }
}
