const operations = document.querySelector('.operations');
	const output_field = document.querySelector('.output_field');

	let temp = '';
	let a=0;
	operations.addEventListener('click', (e) => {
		const value = e.target.dataset['value'];

		if(value !== undefined) {
			if(value == 'ce') {
				temp = '';
				output_field.value = 0;
				return true;
			}
			else if(value == 'x^2'){
				temp =square();
			}
			
			else if(value == 'radic'){
				temp = Math.sqrt(temp);
			}
			else if(value == 'log'){
				temp = Math.log(temp);
			}
			else if(value == 'sin'){
				temp = Math.sin(temp);
			}
			else if(value == 'cos'){
				temp = Math.cos(temp);
			}
			else if(value == 'tan'){
				temp = Math.tan(temp);
			}

			else if(value == '=') {
				const output_fieldwer = eval(temp);
				temp = output_fieldwer;
				
			} else {
				temp += value;
			}

			if(temp == undefined) {
				temp = '';
				output_field.value = 0;
			} else {
				output_field.value = temp;
			}


		}

	});
	const square =()=> {
			return eval(temp*temp);
	}