// let nome = prompt("Como Você Chama?")
//
//
// // "lucas" igual a ''
// if (nome == null) {
//     alert("Recarregue a Pagina")
// } else {
//
//     let correto = confirm("Você Se Chama " + nome + "?")
//
//     if (correto) {
//
//         alert(nome + " Seja Bem-Vindo ao Site de Cursos")
//
//     } else {
//         alert("Recarregue a Pagina")
//     }
// }

function limpaInputsLogin() {
    const inputemail = document.getElementById('input-email')
    const inputsenha = document.getElementById('input-senha')


    inputemail.value = ''
    inputsenha.value = ''
}

function limpaInputsCadastro() {
    const inputnome = document.getElementById('input-nome')
    const inputnascimento = document.getElementById('input-nascimanto')
    const inputcpf = document.getElementById('input-cpf')
    const inputemaill = document.getElementById('input-emaill')
    const inputsenhaa = document.getElementById('input-senhaa')
    const inputcargo = document.getElementById('input-cargo')
    const inputsalario = document.getElementById('input-salario')

    inputnome.value = ''
    inputnascimento.value = ''
    inputcpf.value = ''
    inputemaill.value = ''
    inputsenhaa.value = ''
    inputcargo.value = ''
    inputsalario.value = ''
}


document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener("submit", function (event) {
        //pegar os dois inputs do formulario
        const inputemail = document.getElementById('input-email')
        const inputsenha = document.getElementById('input-senha')

        let temErro = false
        //Verificar se os Inputs Estao vazios

        if (inputemail.value === '') {
            inputemail.classList.add('is-invalid')
            temErro = true
        } else {
            inputemail.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }


        if (inputsenha.value === '') {
            inputsenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputsenha.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }

    })


    const formCadastro = document.getElementById('form-Cadastro')

    formCadastro.addEventListener("submit", function (event) {
        //pegar os dois inputs do formulario
        const inputnome = document.getElementById('input-nome')
        const inputnascimento = document.getElementById('input-nascimanto')
        const inputcpf = document.getElementById('input-cpf')
        const inputemaill = document.getElementById('input-emaill')
        const inputsenhaa = document.getElementById('input-senhaa')
        const inputcargo = document.getElementById('input-cargo')
        const inputsalario = document.getElementById('input-salario')

        let temErro = false
        //Verificar se os Inputs Estao vazios



        if (inputnome.value === '') {
            inputnome.classList.add('is-invalid')
            temErro = true
        } else {
            inputnome.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }


        if (inputnascimento.value === '') {
            inputnascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputnascimento.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }


        if (inputcpf.value === '') {
            inputcpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputcpf.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }


        if (inputemaill.value === '') {
            inputemaill.classList.add('is-invalid')
            temErro = true
        } else {
            inputemaill.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }



        if (inputsenhaa.value === '') {
            inputsenhaa.classList.add('is-invalid')
            temErro = true
        } else {
            inputsenhaa.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }



        if (inputcargo.value === '') {
            inputcargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputcargo.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }



        if (inputsalario.value === '') {
            inputsalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputsalario.classList.remove('is-invalid')

        }

        if (temErro) {
            // Evita de Enviar o Formulario
            event.preventDefault()
            alert("Preencha Todos os Campos")
        }
    })
})