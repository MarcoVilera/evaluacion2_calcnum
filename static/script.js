send = document.querySelector("button")

send.addEventListener("click", async () => {
    try {
        let selectedMatrix = document.querySelector("input[name=op]:checked").value
        if (selectedMatrix === "1")
            selectedMatrix = [
                [4, 3, 5],
                [7, 2, 6],
                [10, 1, 9],
            ]
        if (selectedMatrix === "2")
            selectedMatrix = [
                [10, 9, 7],
                [4, 20, 18],
                [12, 1, -3],
            ]
        if (selectedMatrix === "3")
            selectedMatrix = [
                [15, 9, 12],
                [3, 1, 9],
                [4, 3, 5],
            ]
        console.log(selectedMatrix)
        let selectedFunction = document.querySelector("input[name=func]:checked").value
        let selectedExp = Number(document.querySelector("#exp").value)
        let selectedPE = Number(document.querySelector("#PE").value)
        console.log(selectedPE)
        let selectedPI = Number(document.querySelector("#PI").value)
        console.log(selectedPI)
        if (isNaN(selectedExp)) {
            alert("Por favor ingrese un número en el numero de iteraciones")
            return
        }
        if (isNaN(selectedPE)) {
            alert("Por favor ingrese un número en el punto de expansión")
            return
        }
        if (isNaN(selectedPI)) {
            alert("Por favor ingrese un número en el punto de interpolación")
            return
        }
        //Petición API
        const URL = "http://127.0.0.1:5000/api"

        const data = {
            matrix: selectedMatrix,
            exp: selectedExp,
            function: selectedFunction,
            PE: selectedPE,
            PI: selectedPI,
        }
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }
        try {
            res = await fetch(URL, options)
            json = await res.json()
            console.log(json)
            if (!res.ok) {
                throw "Error en la petición"
            }
            result = document.querySelector(".result")
            result.style.display = "block"

            interpolation = document.querySelector("#interpolation")
            eigen = document.querySelector("#eigen")
            vector = document.querySelector("#vector")

            interpolation.value = json.inter

            eigen.value = json.potSim[0]
            vector.value = json.potSim[1]

        } catch (error) {
            alert("Error en la petición")
        }
    } catch (error) {
        alert("Error enviando datos, por favor comprobar datos ingresados.")
    }

})
