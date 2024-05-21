function showSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
  }
  function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
  }



  if (window.location.hash === '#inscrito') {
    var myModal = new bootstrap.Modal(document.getElementById('inscricaoModal'), {
        keyboard: false
    });
    myModal.show();
}
