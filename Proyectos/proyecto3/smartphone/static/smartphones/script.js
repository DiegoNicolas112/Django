const MyApp = {
    initialize: () => {
        document.getElementById('id_release_date').addEventListener('change', () =>{
            MyApp.checkReleaseDate()
        })
    },
    checkReleaseDate: () =>{
        const releaseDateElement = document.getElementById('id_release_date');
        const inputDate = new Date(releaseDateElement.value);
        const today = new Date();

        inputDate.setHours(0, 0, 0, 0);
        today.setHours(0, 0, 0, 0);
        
        if (inputDate > today) {
            releaseDateElement.setCustomValidity("Fecha pasada de hoy!");
        } else {
            releaseDateElement.setCustomValidity("");
        }

        releaseDateElement.reportValidity();
    }
}


if (document.readyState === 'loading') {
    document.addEventListener('readystatechange', (event) => {
        if (event.target.readyState === 'interactive') {
            MyApp.initialize();
        }
    })
}