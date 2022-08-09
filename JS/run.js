var code = localStorage.getItem("pycode")
localStorage.removeItem("pycode")
document.getElementById("textareaCode").innerHTML = code;
