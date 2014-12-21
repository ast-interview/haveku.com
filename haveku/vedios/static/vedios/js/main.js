


function DoSearch() {
	var v = document.getElementById("search").value;
	
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/search/');
    form.style.display = 'hidden';
    document.body.appendChild(form)
    form.submit();
}











