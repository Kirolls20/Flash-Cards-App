// Filter 
document.getElementById('add-filter').addEventListener('click',function(){
   document.querySelector('.filter-form').style.display = 'flex';

})
document.getElementById('close-btn').addEventListener('click', function() {
   document.querySelector('.filter-form').style.display = 'none';
});