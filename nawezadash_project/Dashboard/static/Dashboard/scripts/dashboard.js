/***
document.addEventListener('DOMContentLoaded', function() {
    const activitiesLink = document.getElementById('activities-link');
    const mainSection = document.getElementById('main-section');
    const activitiesSection = document.getElementById('activities-section');

    activitiesLink.addEventListener('click', function(event) {
        event.preventDefault();

        fetch('/list_activities/')
            .then(response => response.json())
            .then(data => {
                let activitiesHtml = '<h2>Activities</h2><ul>';
                data.activities.forEach(activity => {
                    activitiesHtml += `<li><h3>${activity.name}</h3><p>${activity.description}</p></li>`;
                });
                activitiesHtml += '</ul>';
                activitiesSection.innerHTML = activitiesHtml;
                mainSection.style.display = 'none';
                activitiesSection.style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
});
***/

