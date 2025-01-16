        # # Contract Title
        # contract_title_field = driver.find_element(By.ID, "title")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["contract_title"])
        
        # # Contract Promisor
        # contract_title_field = driver.find_element(By.ID, "promisor")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["promisor"])
        
        # # Contract Promisee
        # contract_title_field = driver.find_element(By.ID, "promisee")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["promisee"])
        

        # # Handle Dropdowns Country
        # country_dropdown_element = driver.find_element(By.XPATH, "//button[.//span[text()='Country']]/following-sibling::select")
        # time.sleep(1)
        # country_select = Select(country_dropdown_element)
        # country_select.select_by_visible_text(contract_data['country'])

        
        # # Handle Dropdowns State
        # state_dropdown_element = driver.find_element(By.XPATH, "//button[.//span[text()='State']]/following-sibling::select")
        # time.sleep(1)
        # state_select = Select(state_dropdown_element)
        # state_select.select_by_visible_text(contract_data['state'])

        
        # # Contract City
        # contract_title_field = driver.find_element(By.ID, "city")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["city"])
        
        # # Contract Value
        # contract_title_field = driver.find_element(By.ID, "contractValue")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["contract_value"])
        
        # # Handle Dropdowns Status
        # status_dropdown_element = driver.find_element(By.XPATH, "//button[.//span[text()='Select a status']]/following-sibling::select")
        # time.sleep(1)
        # status_select = Select(status_dropdown_element)
        # status_select.select_by_visible_text(contract_data['status'])
        
        # # Contract Duration
        # contract_title_field = driver.find_element(By.ID, "contractDuration")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["duration"])
        
        # # Contract Type
        # contract_title_field = driver.find_element(By.ID, "contractType")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["contract_type"])
        
        
        # # Extract and parse the date from contract_data
        # date_value = contract_data["date"]  # Example: "2024-12-01"
        # parsed_date = datetime.strptime(date_value, "%Y-%m-%d")
        # desired_year = parsed_date.year
        # desired_month = parsed_date.strftime("%B")  # Full month name (e.g., "December")
        # desired_day = parsed_date.day

        # # Open the date picker
        # date_picker_elements = driver.find_element(By.CSS_SELECTOR, "svg.lucide-calendar")
        # date_picker_elements.click()
        
        # time.sleep(1)
        # # Locate the SVG element by its class attribute
        # # svg_elements = WebDriverWait(driver, 10).until(
        # #     EC.presence_of_all_elements_located((
        # #         By.CSS_SELECTOR,
        # #         "div#radix-\\:re\\: svg.lucide-chevron-down"
        # #     ))
        # # )

        # # first_svg_element = svg_elements[0]  
        
        # # first_svg_element.click()
        # # time.sleep(5)
        
        # # month_dropdown_element = WebDriverWait(driver, 10).until(
        # #     EC.presence_of_element_located((By.XPATH, "(//div)[last()]"))
        # # )
        
        # # time.sleep(5)

        # # month_element = driver.find_element(By.XPATH, f"//div//*[contains(text(), '{desired_month}')]")
        # # print(month_element.text)

        # # Click on the desired month
        # # month_element.click()
        # # month_item = WebDriverWait(driver, 10).until(
        # #     EC.presence_of_element_located((
        # #         By.XPATH,
        # #         f"//div[last()]//option[normalize-space(text())='{desired_month}']"
        # #     ))
        # # )
        # # logging.info("Desired month item is present. Clicking on the month item...")
        # # month_item.click()
        # # logging.info("Month item clicked successfully.")
        
        # # second_svg_element = svg_elements[1]  
        # # second_svg_element.click()
        # # time.sleep(5)
        # # year_dropdown_element = WebDriverWait(driver, 10).until(
        # #     EC.presence_of_element_located((By.XPATH, "(//div)[last()]"))
        # # )

        

        # # Select the day
        # day_button = WebDriverWait(driver, 1).until(
        #     EC.presence_of_element_located((By.XPATH, f"//div[@id='radix-:re:']//table//button[text()='{desired_day}']"))
        # )
        # day_button.click()


        # # Contract Description
        # contract_title_field = driver.find_element(By.ID, "contractDescription")
        # contract_title_field.clear()
        # contract_title_field.send_keys(contract_data["description"])

        # # Generate the contract
        # submit_button = driver.find_element(By.XPATH, "//button[normalize-space(text())='Generate']")  # Replace with the actual ID
        # submit_button.click()
        
        # logging.info("Login and contract creation completed successfully.")
        
        # time.sleep(15)
        
        # # unlock edit button
        # unlock_button = driver.find_element(By.CLASS_NAME, 'lucide-unlock-keyhole')
        # unlock_button.click()
        # time.sleep(1)
        
        # #edit contract
        # editable_element = driver.find_element(By.CLASS_NAME, 'bn-block-outer')
        # editable_element.send_keys(additional_text)
        # time.sleep(3)
        
        # #download contract
        # download_element = driver.find_element(By.CLASS_NAME, 'lucide-download')
        # download_element.click()      

        # #share contract
        # share_element = driver.find_element(By.XPATH, "//button[normalize-space(text())='Share']")
        # share_element.click()
        
        # try:
        #     share_button = driver.find_element(
        #         By.XPATH, "//button[contains(text(), 'Share') and following-sibling::button[contains(text(), 'Close')]]"
        #     )
        #     share_button.click()
        # except NoSuchElementException:
        #     print("Error: The 'Share' button was not found.")

        # copy_element = driver.find_element(By.CLASS_NAME, 'lucide-copy')
        # copy_element.click()
        
        # contract_link = driver.find_element(By.XPATH, "//input[contains(@id, 'link')]").get_attribute("value")
        # print("Contract link:", contract_link)
        
        # close_element = driver.find_elements(By.TAG_NAME, "button")
        
        # if close_element:
        #     last_button = close_element[-1]  # Access the last button in the list
        #     last_button.click()
        # else:
        #     print("No buttons found on the page.")
        # time.sleep(1)
           
        # profile_element = driver.find_element(By.XPATH, "//button[.//img]")
        # profile_element.click()
        
        # logout_element = driver.find_element(By.XPATH, "//button[normalize-space(text())='Sign Out']")
        # logout_element.click()
        # print("User logged out.")