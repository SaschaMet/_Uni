(() => {

	const inputs = [
		"Team = BAL",
		"Team = CWS",
		"Team = ANA",
		"Team = BOS",
		"Team = CLE",
		"Team = OAK",
		"Team = NYY",
		"Team = DET",
		"Team = SEA",
		"Team = TB",
		"Team = KC",
		"Team = TEX",
		"Team = TOR",
		"Team = MIN",
		"Team = ATL",
		"Team = CHC",
		"Team = ARZ",
		"Team = FLA",
		"Team = CIN",
		"Team = COL",
		"Team = NYM",
		"Team = HOU",
		"Team = LA",
		"Team = PHI",
		"Team = MLW",
		"Team = SD",
		"Team = WAS",
		"Team = PIT",
		"Team = SF",
		"Team = STL",
		"Position = Catcher",
		"Position = First_Baseman",
		"Position = Second_Baseman",
		"Position = Shortstop",
		"Position = Third_Baseman",
		"Position = Outfielder",
		"Position = Designated_Hitter",
		"Position = Starting_Pitcher",
		"Position = Relief_Pitcher",
		"Age"
	]

	// generate the html form
	const form = document.getElementById("inputForm")

	const sampleInput = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,23]

	const generateBooleanInputField = (inputId, labelId, inputName, value) => (
		`
			<div class="col-4 mt-3">
				<label for="${inputId}" id="${labelId}">${inputName}</label>
				<input type="number" min="0" max="1" class="form-control" id="${inputId}" value="${value}">
			</div>
		`
	)

	const generateNumberInputField = (inputId, labelId, inputName, value) => (
		`
			<div class="col-4 mt-3">
				<label for="${inputId}" id="${labelId}">${inputName}</label>
				<input type="number" min="0" max="99" class="form-control" id="${inputId}" value="${value}">
			</div>
		`
	)

	inputs.forEach((input, i) => {
		form.innerHTML += input === "Age" ?
			generateNumberInputField(input, `label-${input}`, input, sampleInput[i]) :
			generateBooleanInputField(input, `label-${input}`, input, sampleInput[i])
	})

	form.innerHTML +=
		`
			<div class="col-12 mt-5">
				<button id="submitButton" class="btn btn-primary">Calculate BMI Score</button>
			</div>
		`

	const submitButton = document.getElementById("submitButton")

	const toggleLoading = (state) => {
		submitButton.disabled = true
		submitButton.textContent = state ? "waiting ..." : "Calculate BMI Score"
	}

	// call the predict route with the input values and get the response
	const predict = () => {
		toggleLoading(true)

		const inputValues = []
		inputs.forEach(input => {
			const inputValue = document.getElementById(input).value
			inputValues.push({[input]: Number(inputValue)})
		})

		fetch('/predict', {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(inputValues),
		})
		.then(async res => {
			res = await res.json()
			toggleLoading(false)
			// add the response
			form.innerHTML +=
			`
				<div class="col-12 mt-5" id="predictions">
					<div class="alert alert-primary" role="alert">
						<p>Prediction linear model: ${Math.round(res.linear)}</p>
					</div>
					<div class="alert alert-primary" role="alert">
						<p>Prediction lasso model: ${Math.round(res.lasso)}</p>
					</div>
				</div>
			`
			setTimeout(() => {
				document.getElementById("predictions").scrollIntoView({behavior: "smooth" })
			}, 300);
			})
		.catch(error => console.error(error))

	}

	// listen for the button click
	submitButton.addEventListener("click", (e) => {
		e.preventDefault()
		console.log("start predicting ...")
		predict()
	});

})()