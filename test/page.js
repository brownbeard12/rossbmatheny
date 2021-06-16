let myCards = document.querySelectorAll('.content');
let rail = document.querySelector('.rail');

rail.addEventListener('click', function(self) {
    
    if (self.target.className === 'content') {
        self.target.velocity({ 'border-color': ['blue', 'white']});
    } else if (self.target.parentNode.className === 'content') {
        self.target.parentNode.velocity({ 'border-color': ['blue', 'white']});
    }
    
    console.log(self.target.parentNode);
    self.stopPropagation();
    
});





/*     Velocity(myCard, {'border-color': ['blue', 'white']}); */