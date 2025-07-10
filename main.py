from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import Optional
from playwright.async_api import async_playwright

app = FastAPI()

class ActionRequest(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    branch_id: Optional[str] = None
    secondary_agent: Optional[str] = None
    loan_program: Optional[str] = None
    internal_program: Optional[str] = None
    prop_process: Optional[str] = None
    primary_status: Optional[str] = None
    lead_source: Optional[str] = None
    referring_party: Optional[str] = None
    pg_one_fname: Optional[str] = None
    pg_one_mname: Optional[str] = None
    pg_one_lname: Optional[str] = None
    pg_one_email: Optional[str] = None
    pg_one_cell: Optional[str] = None
    pg_one_work: Optional[str] = None
    pg_one_street: Optional[str] = None
    pg_one_unit: Optional[str] = None
    pg_one_city: Optional[str] = None
    pg_one_state: Optional[str] = None
    pg_one_zip: Optional[str] = None
    pg_one_county: Optional[str] = None
    pg_one_country: Optional[str] = None
    mailing_street: Optional[str] = None
    mailing_unit: Optional[str] = None
    mailing_city: Optional[str] = None
    mailing_state: Optional[str] = None
    mailing_zip: Optional[str] = None
    mailing_country: Optional[str] = None
    pg_one_dob: Optional[str] = None
    pg_one_ssn: Optional[str] = None
    pg_one_marital_status: Optional[str] = None
    pg_one_citizenship: Optional[str] = None
    pg_one_mid_fico: Optional[str] = None
    pg_one_fico_range: Optional[str] = None
    borrower_type: Optional[str] = None
    entity_name: Optional[str] = None
    trade_name: Optional[str] = None
    entity_type: Optional[str] = None
    date_of_formation: Optional[str] = None
    state_of_formation: Optional[str] = None
    ein_number: Optional[str] = None
    business_phone: Optional[str] = None
    entity_address: Optional[str] = None
    entity_city: Optional[str] = None
    entity_state: Optional[str] = None
    entity_zip: Optional[str] = None
    member_name_zero: Optional[str] = None
    member_title_zero: Optional[str] = None
    member_ownership_zero: Optional[str] = None
    member_address_zero: Optional[str] = None
    member_cell_zero: Optional[str] = None
    member_ssn_zero: Optional[str] = None
    member_dob_zero: Optional[str] = None
    member_email_zero: Optional[str] = None
    member_fico_score_zero: Optional[str] = None
    member_guarantor_zero: Optional[str] = None
    member_citizenship_zero: Optional[str] = None
    member_name_one: Optional[str] = None
    member_title_one: Optional[str] = None
    member_ownership_one: Optional[str] = None
    member_address_one: Optional[str] = None
    member_cell_one: Optional[str] = None
    member_ssn_one: Optional[str] = None
    member_dob_one: Optional[str] = None
    member_email_one: Optional[str] = None
    member_fico_score_one: Optional[str] = None
    member_guarantor_one: Optional[str] = None
    member_citizenship_one: Optional[str] = None
    member_name_two: Optional[str] = None
    member_title_two: Optional[str] = None
    member_ownership_two: Optional[str] = None
    member_address_two: Optional[str] = None
    member_cell_two: Optional[str] = None
    member_ssn_two: Optional[str] = None
    member_dob_two: Optional[str] = None
    member_email_two: Optional[str] = None
    member_fico_score_two: Optional[str] = None
    member_guarantor_two: Optional[str] = None
    member_citizenship_two: Optional[str] = None
    member_name_three: Optional[str] = None
    member_title_three: Optional[str] = None
    member_ownership_three: Optional[str] = None
    member_address_three: Optional[str] = None
    member_cell_three: Optional[str] = None
    member_ssn_three: Optional[str] = None
    member_dob_three: Optional[str] = None
    member_email_three: Optional[str] = None
    member_fico_score_three: Optional[str] = None
    member_guarantor_three: Optional[str] = None
    member_citizenship_three: Optional[str] = None
    member_name_four: Optional[str] = None
    member_title_four: Optional[str] = None
    member_ownership_four: Optional[str] = None
    member_address_four: Optional[str] = None
    member_cell_four: Optional[str] = None
    member_ssn_four: Optional[str] = None
    member_dob_four: Optional[str] = None
    member_email_four: Optional[str] = None
    member_fico_score_four: Optional[str] = None
    member_guarantor_four: Optional[str] = None
    member_citizenship_four: Optional[str] = None
    member_name_five: Optional[str] = None
    member_title_five: Optional[str] = None
    member_ownership_five: Optional[str] = None
    member_address_five: Optional[str] = None
    member_cell_five: Optional[str] = None
    member_ssn_five: Optional[str] = None
    member_dob_five: Optional[str] = None
    member_email_five: Optional[str] = None
    member_fico_score_five: Optional[str] = None
    member_guarantor_five: Optional[str] = None
    member_citizenship_five: Optional[str] = None
    additional_guarantors: Optional[str] = None
    pg_three_fname: Optional[str] = None
    pg_three_mname: Optional[str] = None
    pg_three_lname: Optional[str] = None
    pg_three_cell: Optional[str] = None
    pg_three_ssn: Optional[str] = None
    pg_three_dob: Optional[str] = None
    pg_three_marital_status: Optional[str] = None
    pg_three_street: Optional[str] = None
    pg_three_city: Optional[str] = None
    pg_three_state: Optional[str] = None
    pg_three_zip: Optional[str] = None
    pg_three_email: Optional[str] = None
    pg_three_citizenship: Optional[str] = None
    pg_four_fname: Optional[str] = None
    pg_four_mname: Optional[str] = None
    pg_four_lname: Optional[str] = None
    pg_four_cell: Optional[str] = None
    pg_four_ssn: Optional[str] = None
    pg_four_dob: Optional[str] = None
    pg_four_marital_status: Optional[str] = None
    pg_four_street: Optional[str] = None
    pg_four_city: Optional[str] = None
    pg_four_state: Optional[str] = None
    pg_four_zip: Optional[str] = None
    pg_four_email: Optional[str] = None
    pg_four_citizenship: Optional[str] = None
    is_bankrupt: Optional[str] = None
    is_outstanding_judgement: Optional[str] = None
    is_active_lawsuit: Optional[str] = None
    is_forclosure: Optional[str] = None
    is_delinquent: Optional[str] = None
    is_fraud: Optional[str] = None
    borrower_designated_beneficiary: Optional[str] = None
    flip_experience: Optional[str] = None
    flips_completed: Optional[str] = None
    ground_up_experience: Optional[str] = None
    ground_ups_completed: Optional[str] = None
    is_borrower_gc: Optional[str] = None
    rental_experience: Optional[str] = None
    rentals_owned: Optional[str] = None
    have_professional_licences: Optional[str] = None
    professional_licences: Optional[str] = None
    liquid_assets: Optional[str] = None
    desired_closing_date: Optional[str] = None
    desired_loan_amount: Optional[str] = None
    type_of_loan_requesting: Optional[str] = None
    trial_payment_date: Optional[str] = None
    maturity_date: Optional[str] = None
    loan_term: Optional[str] = None
    interest_rate: Optional[str] = None
    lien_terms: Optional[str] = None
    amortization_type: Optional[str] = None
    is_taxes_ins_escrowed: Optional[str] = None
    taxes: Optional[str] = None
    annual_premium: Optional[str] = None
    cost_basis: Optional[str] = None
    home_value: Optional[str] = None
    max_amount_to_put_down: Optional[str] = None
    subject_property_address: Optional[str] = None
    subject_property_unit: Optional[str] = None
    subject_property_city: Optional[str] = None
    subject_property_state: Optional[str] = None
    subject_property_zip: Optional[str] = None
    subject_property_county: Optional[str] = None
    subject_property_apn: Optional[str] = None
    subject_property_block: Optional[str] = None
    subject_property_lot: Optional[str] = None
    subject_property_type: Optional[str] = None
    subject_property_sqft: Optional[str] = None
    subject_property_acres: Optional[str] = None
    subject_property_year_built: Optional[str] = None
    bedrooms: Optional[str] = None
    bathrooms: Optional[str] = None
    half_bathrooms: Optional[str] = None
    number_of_buildings: Optional[str] = None
    number_of_units_occupied: Optional[str] = None
    number_of_parcels: Optional[str] = None
    estimated_property_value: Optional[str] = None
    present_occupancy: Optional[str] = None
    lb_contact_name: Optional[str] = None
    lb_contact_email: Optional[str] = None
    lb_contact_phone: Optional[str] = None
    unit_type_1_1: Optional[str] = None
    unit_num_1_1: Optional[str] = None
    sq_ft_1_1: Optional[str] = None
    rent_roll_market_rents_1_1: Optional[str] = None
    rent_roll_actual_rents_1_1: Optional[str] = None
    rent_roll_monthly_rent_1_1: Optional[str] = None
    rent_roll_vacant_no_1_1: Optional[str] = None
    unit_type_1_2: Optional[str] = None
    unit_num_1_2: Optional[str] = None
    sq_ft_1_2: Optional[str] = None
    rent_roll_market_rents_1_2: Optional[str] = None
    rent_roll_actual_rents_1_2: Optional[str] = None
    rent_roll_monthly_rent_1_2: Optional[str] = None
    rent_roll_vacant_no_1_2: Optional[str] = None
    unit_type_1_3: Optional[str] = None
    unit_num_1_3: Optional[str] = None
    sq_ft_1_3: Optional[str] = None
    rent_roll_market_rents_1_3: Optional[str] = None
    rent_roll_actual_rents_1_3: Optional[str] = None
    rent_roll_monthly_rent_1_3: Optional[str] = None
    rent_roll_vacant_no_1_3: Optional[str] = None
    unit_type_1_4: Optional[str] = None
    unit_num_1_4: Optional[str] = None
    sq_ft_1_4: Optional[str] = None
    rent_roll_market_rents_1_4: Optional[str] = None
    rent_roll_actual_rents_1_4: Optional[str] = None
    rent_roll_monthly_rent_1_4: Optional[str] = None
    rent_roll_vacant_no_1_4: Optional[str] = None
    unit_type_1_5: Optional[str] = None
    unit_num_1_5: Optional[str] = None
    sq_ft_1_5: Optional[str] = None
    rent_roll_market_rents_1_5: Optional[str] = None
    rent_roll_actual_rents_1_5: Optional[str] = None
    rent_roll_monthly_rent_1_5: Optional[str] = None
    rent_roll_vacant_no_1_5: Optional[str] = None
    unit_type_1_6: Optional[str] = None
    unit_num_1_6: Optional[str] = None
    sq_ft_1_6: Optional[str] = None
    rent_roll_market_rents_1_6: Optional[str] = None
    rent_roll_actual_rents_1_6: Optional[str] = None
    rent_roll_monthly_rent_1_6: Optional[str] = None
    rent_roll_vacant_no_1_6: Optional[str] = None
    unit_type_1_7: Optional[str] = None
    unit_num_1_7: Optional[str] = None
    sq_ft_1_7: Optional[str] = None
    rent_roll_market_rents_1_7: Optional[str] = None
    rent_roll_actual_rents_1_7: Optional[str] = None
    rent_roll_monthly_rent_1_7: Optional[str] = None
    rent_roll_vacant_no_1_7: Optional[str] = None
    unit_type_1_8: Optional[str] = None
    unit_num_1_8: Optional[str] = None
    sq_ft_1_8: Optional[str] = None
    rent_roll_market_rents_1_8: Optional[str] = None
    rent_roll_actual_rents_1_8: Optional[str] = None
    rent_roll_monthly_rent_1_8: Optional[str] = None
    rent_roll_vacant_no_1_8: Optional[str] = None
    unit_type_1_9: Optional[str] = None
    unit_num_1_9: Optional[str] = None
    sq_ft_1_9: Optional[str] = None
    rent_roll_market_rents_1_9: Optional[str] = None
    rent_roll_actual_rents_1_9: Optional[str] = None
    rent_roll_monthly_rent_1_9: Optional[str] = None
    rent_roll_vacant_no_1_9: Optional[str] = None
    unit_type_1_10: Optional[str] = None
    unit_num_1_10: Optional[str] = None
    sq_ft_1_10: Optional[str] = None
    rent_roll_market_rents_1_10: Optional[str] = None
    rent_roll_actual_rents_1_10: Optional[str] = None
    rent_roll_monthly_rent_1_10: Optional[str] = None
    rent_roll_vacant_no_1_10: Optional[str] = None
    is_hoa_available_yes_1_is_hoa_available: Optional[str] = None
    monthly_hoa_fees: Optional[str] = None
    actual_rents_in_place: Optional[str] = None
    spcf_hoafees: Optional[str] = None
    is_bor_intend_to_occupy_prop_as_pri_no: Optional[str] = None
    is_co_bor_intend_to_occupy_prop_as_pri_no: Optional[str] = None
    title_seller: Optional[str] = None
    title_name: Optional[str] = None
    title_order_number: Optional[str] = None
    pro_ins_first_name_1: Optional[str] = None
    pro_ins_last_name_1: Optional[str] = None
    pro_ins_name_1: Optional[str] = None
    pro_inc_email_1: Optional[str] = None
    pro_inc_ph_1: Optional[str] = None

async def run_playwright_actions(request: ActionRequest):
    results = []
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(viewport={'width': 1280, 'height': 720})
            page = await context.new_page()
            # --- Start of user-specified actions ---
            await page.goto("https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help")
            results.append("Navigated to BRRRR backoffice login")
            await page.wait_for_selector('input#userName', timeout=10000)
            results.append("Waited for username input")
            email_field = page.locator('input#userName')
            await email_field.click()
            results.append("Clicked username field")
            if request.username is not None:
                await email_field.fill(request.username)
                results.append(f"Filled username with {request.username}")
            pwd_input = page.locator('input#pwd')
            await pwd_input.wait_for(timeout=10000)
            results.append("Waited for password input")
            await pwd_input.click()
            results.append("Clicked password field")
            if request.password is not None:
                await pwd_input.fill(request.password)
                results.append(f"Filled password with {request.password}")
            await page.click("button#submitbutton")
            results.append("Clicked login button")
            await page.wait_for_url("https://app.brrrr.com/backoffice/LMRequest*", timeout=20000)
            results.append("Waited for post-login URL")
            if request.branch_id is not None:
                await page.select_option('select#branchId', value=request.branch_id)
                results.append(f"Selected branchId with {request.branch_id}")
            if request.secondary_agent is not None:
                await page.select_option('select#secondaryAgentId', label=request.secondary_agent)
                results.append(f"Selected secondaryAgentId with {request.secondary_agent}")
            await page.click('div#LMRClientType_chosen')
            results.append("Clicked LMRClientType_chosen")
            if request.loan_program is not None:
                await page.click(f'ul.chosen-results li.active-result:has-text("{request.loan_program}")')
                results.append(f"Selected loan program {request.loan_program}")
            await page.click('div#LMRInternalLoanProgram_chosen')
            results.append("Clicked LMRInternalLoanProgram_chosen")
            if request.internal_program is not None:
                await page.click(f'ul.chosen-results li.active-result:has-text("{request.internal_program}")')
                results.append(f"Selected internal program {request.internal_program}")
            if request.prop_process is not None:
                await page.select_option('#propDetailsProcess', value=request.prop_process)
                results.append(f"Selected propDetailsProcess with {request.prop_process}")
            if request.primary_status is not None:
                await page.select_option('#primaryStatus', value=request.primary_status)
                results.append(f"Selected primaryStatus with {request.primary_status}")
            if request.lead_source is not None:
                await page.fill('#leadSource', value=request.lead_source)
                results.append(f"Filled leadSource with {request.lead_source}")
            if request.referring_party is not None:
                await page.fill('#referringParty', value=request.referring_party)
                results.append(f"Filled referringParty with {request.referring_party}")
            if request.pg_one_fname is not None:
                await page.fill('#borrowerFName', value=request.pg_one_fname)
                results.append(f"Filled borrowerFName with {request.pg_one_fname}")
            if request.pg_one_mname is not None:
                await page.fill('#borrowerMName', value=request.pg_one_mname)
                results.append(f"Filled borrowerMName with {request.pg_one_mname}")
            if request.pg_one_lname is not None:
                await page.fill('#borrowerLName', value=request.pg_one_lname)
                results.append(f"Filled borrowerLName with {request.pg_one_lname}")
            if request.pg_one_email is not None:
                await page.fill('#borrowerEmail', value=request.pg_one_email)
                results.append(f"Filled borrowerEmail with {request.pg_one_email}")
            if request.pg_one_cell is not None:
                await page.fill('#cellNo', value=request.pg_one_cell)
                results.append(f"Filled cellNo with {request.pg_one_cell}")
            if request.pg_one_work is not None:
                await page.fill('#workNumber', value=request.pg_one_work)
                results.append(f"Filled workNumber with {request.pg_one_work}")
            if request.pg_one_street is not None:
                await page.fill('#presentAddress', value=request.pg_one_street)
                results.append(f"Filled presentAddress with {request.pg_one_street}")
            if request.pg_one_unit is not None:
                await page.fill('#presentUnit', value=request.pg_one_unit)
                results.append(f"Filled presentUnit with {request.pg_one_unit}")
            if request.pg_one_city is not None:
                await page.fill('#presentCity', value=request.pg_one_city)
                results.append(f"Filled presentCity with {request.pg_one_city}")
            if request.pg_one_state is not None:
                await page.select_option('#presentState', value=request.pg_one_state)
                results.append(f"Selected presentState with {request.pg_one_state}")
            if request.pg_one_zip is not None:
                await page.fill('#presentZip', value=request.pg_one_zip)
                results.append(f"Filled presentZip with {request.pg_one_zip}")
            if request.pg_one_county is not None:
                await page.select_option('#presentCounty', value=request.pg_one_county)
                results.append(f"Selected presentCounty with {request.pg_one_county}")
            if request.pg_one_country is not None:
                await page.select_option('#presentCountry', value=request.pg_one_country)
                results.append(f"Selected presentCountry with {request.pg_one_country}")
            if request.mailing_street is not None:
                await page.fill('#mailingAddress', value=request.mailing_street)
                results.append(f"Filled mailingAddress with {request.mailing_street}")
            if request.mailing_unit is not None:
                await page.fill('#mailingUnit', value=request.mailing_unit)
                results.append(f"Filled mailingUnit with {request.mailing_unit}")
            if request.mailing_city is not None:
                await page.fill('#mailingCity', value=request.mailing_city)
                results.append(f"Filled mailingCity with {request.mailing_city}")
            if request.mailing_state is not None:
                await page.select_option('#mailingState', value=request.mailing_state)
                results.append(f"Selected mailingState with {request.mailing_state}")
            if request.mailing_zip is not None:
                await page.fill('#mailingZip', value=request.mailing_zip)
                results.append(f"Filled mailingZip with {request.mailing_zip}")
            if request.mailing_country is not None:
                await page.select_option('#mailingCountry', value=request.mailing_country)
                results.append(f"Selected mailingCountry with {request.mailing_country}")
            if request.pg_one_dob is not None:
                await page.fill('#borrowerDOB', value=request.pg_one_dob)
                results.append(f"Filled borrowerDOB with {request.pg_one_dob}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after DOB")
            if request.pg_one_ssn is not None:
                await page.fill('#ssn', value=request.pg_one_ssn)
                results.append(f"Filled ssn with {request.pg_one_ssn}")
            if request.pg_one_marital_status is not None:
                await page.wait_for_selector(f'label[for="{request.pg_one_marital_status}"]', timeout=10000)
                await page.click(f'label[for="{request.pg_one_marital_status}"]')
                results.append(f"Clicked marital status {request.pg_one_marital_status}")
            if request.pg_one_citizenship is not None:
                await page.wait_for_selector(f'label[for="{request.pg_one_citizenship}"]', timeout=10000)
                await page.click(f'label[for="{request.pg_one_citizenship}"]')
                results.append(f"Clicked citizenship {request.pg_one_citizenship}")
            if request.pg_one_mid_fico is not None:
                await page.fill('#midFicoScore', value=request.pg_one_mid_fico)
                results.append(f"Filled midFicoScore with {request.pg_one_mid_fico}")
            if request.pg_one_fico_range is not None:
                await page.select_option('#borCreditScoreRange', value=request.pg_one_fico_range)
                results.append(f"Selected borCreditScoreRange with {request.pg_one_fico_range}")
            if request.borrower_type is not None:
                await page.select_option('#borrowerType', value=request.borrower_type)
                results.append(f"Selected borrowerType with {request.borrower_type}")
            if request.entity_name is not None:
                await page.fill('#entityName', value=request.entity_name)
                results.append(f"Filled entityName with {request.entity_name}")
            if request.trade_name is not None:
                await page.fill('#tradeName', value=request.trade_name)
                results.append(f"Filled tradeName with {request.trade_name}")
            if request.entity_type is not None:
                await page.select_option('#entityType', value=request.entity_type)
                results.append(f"Selected entityType with {request.entity_type}")
            if request.date_of_formation is not None:
                await page.fill('#dateOfFormation', value=request.date_of_formation)
                results.append(f"Filled dateOfFormation with {request.date_of_formation}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after dateOfFormation")
            if request.state_of_formation is not None:
                await page.select_option('#entityStateOfFormation', value=request.state_of_formation)
                results.append(f"Selected entityStateOfFormation with {request.state_of_formation}")
            if request.ein_number is not None:
                await page.fill('#ENINo', value=request.ein_number)
                results.append(f"Filled ENINo with {request.ein_number}")
            if request.business_phone is not None:
                await page.fill('#businessPhone', value=request.business_phone)
                results.append(f"Filled businessPhone with {request.business_phone}")
            if request.entity_address is not None:
                await page.fill('#entityAddress', value=request.entity_address)
                results.append(f"Filled entityAddress with {request.entity_address}")
            if request.entity_city is not None:
                await page.fill('#entityCity', value=request.entity_city)
                results.append(f"Filled entityCity with {request.entity_city}")
            if request.entity_state is not None:
                await page.select_option('#entityState', value=request.entity_state)
                results.append(f"Selected entityState with {request.entity_state}")
            if request.entity_zip is not None:
                await page.fill('#entityZip', value=request.entity_zip)
                results.append(f"Filled entityZip with {request.entity_zip}")
            # Member 0
            if request.member_name_zero is not None:
                await page.fill('#memberName0', value=request.member_name_zero)
                results.append(f"Filled #memberName0 with {request.member_name_zero}")
            if request.member_title_zero is not None:
                await page.fill('#memberTitle0', value=request.member_title_zero)
                results.append(f"Filled #memberTitle0 with {request.member_title_zero}")
            if request.member_ownership_zero is not None:
                await page.fill('#memberOwnership0', value=request.member_ownership_zero)
                results.append(f"Filled #memberOwnership0 with {request.member_ownership_zero}")
            if request.member_address_zero is not None:
                await page.fill('#memberAddress0', value=request.member_address_zero)
                results.append(f"Filled #memberAddress0 with {request.member_address_zero}")
            if request.member_cell_zero is not None:
                await page.fill('#memberCell0', value=request.member_cell_zero)
                results.append(f"Filled #memberCell0 with {request.member_cell_zero}")
            if request.member_ssn_zero is not None:
                await page.fill('#memberSSN0', value=request.member_ssn_zero)
                results.append(f"Filled #memberSSN0 with {request.member_ssn_zero}")
            if request.member_dob_zero is not None:
                await page.fill('#memberDOB0', value=request.member_dob_zero)
                results.append(f"Filled #memberDOB0 with {request.member_dob_zero}")
            await page.click('body', position={'x': 10, 'y': 10})
            results.append("Clicked body after memberDOB0")
            if request.member_email_zero is not None:
                await page.fill('#memberEmail0', value=request.member_email_zero)
                results.append(f"Filled #memberEmail0 with {request.member_email_zero}")
            if request.member_fico_score_zero is not None:
                await page.fill('#memberCreditScore0', value=request.member_fico_score_zero)
                results.append(f"Filled #memberCreditScore0 with {request.member_fico_score_zero}")
            if request.member_guarantor_zero is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_zero}"]', timeout=10000)
                await page.click(f'label[for="{request.member_guarantor_zero}"]')
                results.append(f"Clicked label for {request.member_guarantor_zero}")
            if request.member_citizenship_zero is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_zero}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_zero}"]')
                results.append(f"Clicked label for {request.member_citizenship_zero}")
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (0)")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new member form (0)")

            # Member 1
            if request.member_name_one is not None:
                await page.fill('#memberName1', value=request.member_name_one)
                results.append(f"Filled #memberName1 with {request.member_name_one}")
            if request.member_title_one is not None:
                await page.fill('#memberTitle1', value=request.member_title_one)
                results.append(f"Filled #memberTitle1 with {request.member_title_one}")
            if request.member_ownership_one is not None:
                await page.fill('#memberOwnership1', value=request.member_ownership_one)
                results.append(f"Filled #memberOwnership1 with {request.member_ownership_one}")
            if request.member_address_one is not None:
                await page.fill('#memberAddress1', value=request.member_address_one)
                results.append(f"Filled #memberAddress1 with {request.member_address_one}")
            if request.member_cell_one is not None:
                await page.fill('#memberCell1', value=request.member_cell_one)
                results.append(f"Filled #memberCell1 with {request.member_cell_one}")
            if request.member_ssn_one is not None:
                await page.fill('#memberSSN1', value=request.member_ssn_one)
                results.append(f"Filled #memberSSN1 with {request.member_ssn_one}")
            if request.member_dob_one is not None:
                await page.fill('#memberDOB1', value=request.member_dob_one)
                results.append(f"Filled #memberDOB1 with {request.member_dob_one}")
            await page.click('body', position={'x': 10, 'y': 10})
            results.append("Clicked body after memberDOB1")
            if request.member_email_one is not None:
                await page.fill('#memberEmail1', value=request.member_email_one)
                results.append(f"Filled #memberEmail1 with {request.member_email_one}")
            if request.member_fico_score_one is not None:
                await page.fill('#memberCreditScore1', value=request.member_fico_score_one)
                results.append(f"Filled #memberCreditScore1 with {request.member_fico_score_one}")
            if request.member_guarantor_one is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_one}"]', timeout=10000)
                await page.click(f'label[for="{request.member_guarantor_one}"]')
                results.append(f"Clicked label for {request.member_guarantor_one}")
            if request.member_citizenship_one is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_one}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_one}"]')
                results.append(f"Clicked label for {request.member_citizenship_one}")
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (1)")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new member form (1)")

            # After member_citizenship_one
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (2)")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new member form (2)")
            if request.member_name_two is not None:
                await page.fill('#memberName2', value=request.member_name_two)
                results.append(f"Filled #memberName2 with {request.member_name_two}")
            if request.member_title_two is not None:
                await page.fill('#memberTitle2', value=request.member_title_two)
                results.append(f"Filled #memberTitle2 with {request.member_title_two}")
            if request.member_ownership_two is not None:
                await page.fill('#memberOwnership2', value=request.member_ownership_two)
                results.append(f"Filled #memberOwnership2 with {request.member_ownership_two}")
            if request.member_address_two is not None:
                await page.fill('#memberAddress2', value=request.member_address_two)
                results.append(f"Filled #memberAddress2 with {request.member_address_two}")
            if request.member_cell_two is not None:
                await page.fill('#memberCell2', value=request.member_cell_two)
                results.append(f"Filled #memberCell2 with {request.member_cell_two}")
            if request.member_ssn_two is not None:
                await page.fill('#memberSSN2', value=request.member_ssn_two)
                results.append(f"Filled #memberSSN2 with {request.member_ssn_two}")
            if request.member_dob_two is not None:
                await page.fill('#memberDOB2', value=request.member_dob_two)
                results.append(f"Filled #memberDOB2 with {request.member_dob_two}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after memberDOB2")
            if request.member_email_two is not None:
                await page.fill('#memberEmail2', value=request.member_email_two)
                results.append(f"Filled #memberEmail2 with {request.member_email_two}")
            if request.member_fico_score_two is not None:
                await page.fill('#memberCreditScore2', value=request.member_fico_score_two)
                results.append(f"Filled #memberCreditScore2 with {request.member_fico_score_two}")
            if request.member_guarantor_two is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_two}"]', timeout=10000)
                await page.click(f'label[for="{request.member_guarantor_two}"]')
                results.append(f"Clicked label for {request.member_guarantor_two}")
            if request.member_citizenship_two is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_two}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_two}"]')
                results.append(f"Clicked label for {request.member_citizenship_two}")
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (3)")
            if request.member_name_three is not None:
                await page.fill('#memberName3', value=request.member_name_three)
                results.append(f"Filled #memberName3 with {request.member_name_three}")
            if request.member_title_three is not None:
                await page.fill('#memberTitle3', value=request.member_title_three)
                results.append(f"Filled #memberTitle3 with {request.member_title_three}")
            if request.member_ownership_three is not None:
                await page.fill('#memberOwnership3', value=request.member_ownership_three)
                results.append(f"Filled #memberOwnership3 with {request.member_ownership_three}")
            if request.member_address_three is not None:
                await page.fill('#memberAddress3', value=request.member_address_three)
                results.append(f"Filled #memberAddress3 with {request.member_address_three}")
            if request.member_cell_three is not None:
                await page.fill('#memberCell3', value=request.member_cell_three)
                results.append(f"Filled #memberCell3 with {request.member_cell_three}")
            if request.member_ssn_three is not None:
                await page.fill('#memberSSN3', value=request.member_ssn_three)
                results.append(f"Filled #memberSSN3 with {request.member_ssn_three}")
            if request.member_dob_three is not None:
                await page.fill('#memberDOB3', value=request.member_dob_three)
                results.append(f"Filled #memberDOB3 with {request.member_dob_three}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after memberDOB3")
            if request.member_email_three is not None:
                await page.fill('#memberEmail3', value=request.member_email_three)
                results.append(f"Filled #memberEmail3 with {request.member_email_three}")
            if request.member_fico_score_three is not None:
                await page.fill('#memberCreditScore3', value=request.member_fico_score_three)
                results.append(f"Filled #memberCreditScore3 with {request.member_fico_score_three}")
            if request.member_guarantor_three is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_three}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_three}"]')
                results.append(f"Clicked label for {request.member_guarantor_three}")
            if request.member_citizenship_three is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_three}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_three}"]')
                results.append(f"Clicked label for {request.member_citizenship_three}")
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (4)")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new member form (4)")
            if request.member_name_four is not None:
                await page.fill('#memberName4', value=request.member_name_four)
                results.append(f"Filled #memberName4 with {request.member_name_four}")
            if request.member_title_four is not None:
                await page.fill('#memberTitle4', value=request.member_title_four)
                results.append(f"Filled #memberTitle4 with {request.member_title_four}")
            if request.member_ownership_four is not None:
                await page.fill('#memberOwnership4', value=request.member_ownership_four)
                results.append(f"Filled #memberOwnership4 with {request.member_ownership_four}")
            if request.member_address_four is not None:
                await page.fill('#memberAddress4', value=request.member_address_four)
                results.append(f"Filled #memberAddress4 with {request.member_address_four}")
            if request.member_cell_four is not None:
                await page.fill('#memberCell4', value=request.member_cell_four)
                results.append(f"Filled #memberCell4 with {request.member_cell_four}")
            if request.member_ssn_four is not None:
                await page.fill('#memberSSN4', value=request.member_ssn_four)
                results.append(f"Filled #memberSSN4 with {request.member_ssn_four}")
            if request.member_dob_four is not None:
                await page.fill('#memberDOB4', value=request.member_dob_four)
                results.append(f"Filled #memberDOB4 with {request.member_dob_four}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after memberDOB4")
            if request.member_email_four is not None:
                await page.fill('#memberEmail4', value=request.member_email_four)
                results.append(f"Filled #memberEmail4 with {request.member_email_four}")
            if request.member_fico_score_four is not None:
                await page.fill('#memberCreditScore4', value=request.member_fico_score_four)
                results.append(f"Filled #memberCreditScore4 with {request.member_fico_score_four}")
            if request.member_guarantor_four is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_four}"]', timeout=10000)
                await page.click(f'label[for="{request.member_guarantor_four}"]')
                results.append(f"Clicked label for {request.member_guarantor_four}")
            if request.member_citizenship_four is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_four}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_four}"]')
                results.append(f"Clicked label for {request.member_citizenship_four}")
            await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
            results.append("Clicked add member/officer (5)")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new member form (5)")
            if request.member_name_five is not None:
                await page.fill('#memberName5', value=request.member_name_five)
                results.append(f"Filled #memberName5 with {request.member_name_five}")
            if request.member_title_five is not None:
                await page.fill('#memberTitle5', value=request.member_title_five)
                results.append(f"Filled #memberTitle5 with {request.member_title_five}")
            if request.member_ownership_five is not None:
                await page.fill('#memberOwnership5', value=request.member_ownership_five)
                results.append(f"Filled #memberOwnership5 with {request.member_ownership_five}")
            if request.member_address_five is not None:
                await page.fill('#memberAddress5', value=request.member_address_five)
                results.append(f"Filled #memberAddress5 with {request.member_address_five}")
            if request.member_cell_five is not None:
                await page.fill('#memberCell5', value=request.member_cell_five)
                results.append(f"Filled #memberCell5 with {request.member_cell_five}")
            if request.member_ssn_five is not None:
                await page.fill('#memberSSN5', value=request.member_ssn_five)
                results.append(f"Filled #memberSSN5 with {request.member_ssn_five}")
            if request.member_dob_five is not None:
                await page.fill('#memberDOB5', value=request.member_dob_five)
                results.append(f"Filled #memberDOB5 with {request.member_dob_five}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after memberDOB5")
            if request.member_email_five is not None:
                await page.fill('#memberEmail5', value=request.member_email_five)
                results.append(f"Filled #memberEmail5 with {request.member_email_five}")
            if request.member_fico_score_five is not None:
                await page.fill('#memberCreditScore5', value=request.member_fico_score_five)
                results.append(f"Filled #memberCreditScore5 with {request.member_fico_score_five}")
            if request.member_guarantor_five is not None:
                await page.wait_for_selector(f'label[for="{request.member_guarantor_five}"]', timeout=10000)
                await page.click(f'label[for="{request.member_guarantor_five}"]')
                results.append(f"Clicked label for {request.member_guarantor_five}")
            if request.member_citizenship_five is not None:
                await page.wait_for_selector(f'label[for="{request.member_citizenship_five}"]', timeout=10000)
                await page.click(f'label[for="{request.member_citizenship_five}"]')
                results.append(f"Clicked label for {request.member_citizenship_five}")

            # After member_citizenship_five
            if request.additional_guarantors is not None and request.additional_guarantors.strip() != "":
                await page.wait_for_selector(f'label[for="{request.additional_guarantors}"]', timeout=10000)
                await page.click(f'label[for="{request.additional_guarantors}"]')
                results.append(f"Clicked label for {request.additional_guarantors}")
            if request.pg_three_fname is not None:
                await page.fill('#guarantorFName', value=request.pg_three_fname)
                results.append(f"Filled #guarantorFName with {request.pg_three_fname}")
            if request.pg_three_mname is not None:
                await page.fill('#guarantorMName', value=request.pg_three_mname)
                results.append(f"Filled #guarantorMName with {request.pg_three_mname}")
            if request.pg_three_lname is not None:
                await page.fill('#guarantorLName', value=request.pg_three_lname)
                results.append(f"Filled #guarantorLName with {request.pg_three_lname}")
            if request.pg_three_cell is not None:
                await page.fill('#guarantorCellNumber', value=request.pg_three_cell)
                results.append(f"Filled #guarantorCellNumber with {request.pg_three_cell}")
            if request.pg_three_ssn is not None:
                await page.fill('#guarantorSSN', value=request.pg_three_ssn)
                results.append(f"Filled #guarantorSSN with {request.pg_three_ssn}")
            if request.pg_three_dob is not None:
                await page.fill('#guarantorDOB', value=request.pg_three_dob)
                results.append(f"Filled #guarantorDOB with {request.pg_three_dob}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after pg_three_dob")
            if request.pg_three_marital_status is not None:
                await page.select_option('#guarantorStatus', value=request.pg_three_marital_status)
                results.append(f"Selected #guarantorStatus with {request.pg_three_marital_status}")
            if request.pg_three_street is not None:
                await page.fill('#guarantorAddress', value=request.pg_three_street)
                results.append(f"Filled #guarantorAddress with {request.pg_three_street}")
            if request.pg_three_city is not None:
                await page.fill('#guarantorCity', value=request.pg_three_city)
                results.append(f"Filled #guarantorCity with {request.pg_three_city}")
            if request.pg_three_state is not None:
                await page.select_option('#guarantorState', value=request.pg_three_state)
                results.append(f"Selected #guarantorState with {request.pg_three_state}")
            if request.pg_three_zip is not None:
                await page.fill('#guarantorZip', value=request.pg_three_zip)
                results.append(f"Filled #guarantorZip with {request.pg_three_zip}")
            if request.pg_three_email is not None:
                await page.fill('#guarantorEmail', value=request.pg_three_email)
                results.append(f"Filled #guarantorEmail with {request.pg_three_email}")
            if request.pg_three_citizenship is not None:
                await page.wait_for_selector(f'label[for="{request.pg_three_citizenship}"]', timeout=10000)
                await page.click(f'label[for="{request.pg_three_citizenship}"]')
                results.append(f"Clicked label for {request.pg_three_citizenship}")
            if request.additional_guarantors is not None and request.additional_guarantors.strip() != "":
                await page.wait_for_timeout(1000)
                results.append("Waited 1s for new member form (guarantor)")
                await page.wait_for_selector('a[onclick*="addOrRemoveAdditionalGuarantors"]', timeout=10000)
                await page.click('a[onclick*="addOrRemoveAdditionalGuarantors"]')
                results.append("Clicked addOrRemoveAdditionalGuarantors link")
                await page.wait_for_timeout(1000)
                results.append("Waited 1s for new member form (guarantor 1)")
            if request.pg_four_fname is not None:
                await page.fill('#guarantorFName_1', value=request.pg_four_fname)
                results.append(f"Filled #guarantorFName_1 with {request.pg_four_fname}")
            if request.pg_four_mname is not None:
                await page.fill('#guarantorMName_1', value=request.pg_four_mname)
                results.append(f"Filled #guarantorMName_1 with {request.pg_four_mname}")
            if request.pg_four_lname is not None:
                await page.fill('#guarantorLName_1', value=request.pg_four_lname)
                results.append(f"Filled #guarantorLName_1 with {request.pg_four_lname}")
            if request.pg_four_cell is not None:
                await page.fill('#guarantorCellNumber_1', value=request.pg_four_cell)
                results.append(f"Filled #guarantorCellNumber_1 with {request.pg_four_cell}")
            if request.pg_four_ssn is not None:
                await page.fill('#guarantorSSN_1', value=request.pg_four_ssn)
                results.append(f"Filled #guarantorSSN_1 with {request.pg_four_ssn}")
            if request.pg_four_dob is not None:
                await page.fill('#guarantorDOB_1', value=request.pg_four_dob)
                results.append(f"Filled #guarantorDOB_1 with {request.pg_four_dob}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after pg_four_dob")
            if request.pg_four_marital_status is not None:
                await page.select_option('#guarantorStatus_1', value=request.pg_four_marital_status)
                results.append(f"Selected #guarantorStatus_1 with {request.pg_four_marital_status}")
            if request.pg_four_street is not None:
                await page.fill('#guarantorAddress_1', value=request.pg_four_street)
                results.append(f"Filled #guarantorAddress_1 with {request.pg_four_street}")
            if request.pg_four_city is not None:
                await page.fill('#guarantorCity_1', value=request.pg_four_city)
                results.append(f"Filled #guarantorCity_1 with {request.pg_four_city}")
            if request.pg_four_state is not None:
                await page.select_option('#guarantorState_1', value=request.pg_four_state)
                results.append(f"Selected #guarantorState_1 with {request.pg_four_state}")
            if request.pg_four_zip is not None:
                await page.fill('#guarantorZip_1', value=request.pg_four_zip)
                results.append(f"Filled #guarantorZip_1 with {request.pg_four_zip}")
            if request.pg_four_email is not None:
                await page.fill('#guarantorEmail_1', value=request.pg_four_email)
                results.append(f"Filled #guarantorEmail_1 with {request.pg_four_email}")
            if request.pg_four_citizenship is not None:
                await page.wait_for_selector(f'label[for="{request.pg_four_citizenship}"]', timeout=10000)
                await page.click(f'label[for="{request.pg_four_citizenship}"]')
                results.append(f"Clicked label for {request.pg_four_citizenship}")
            if request.is_bankrupt is not None:
                await page.wait_for_selector(f'label[for="{request.is_bankrupt}"]', timeout=10000)
                await page.click(f'label[for="{request.is_bankrupt}"]')
                results.append(f"Clicked label for {request.is_bankrupt}")
            if request.is_outstanding_judgement is not None:
                await page.wait_for_selector(f'label[for="{request.is_outstanding_judgement}"]', timeout=10000)
                await page.click(f'label[for="{request.is_outstanding_judgement}"]')
                results.append(f"Clicked label for {request.is_outstanding_judgement}")
            if request.is_active_lawsuit is not None:
                await page.wait_for_selector(f'label[for="{request.is_active_lawsuit}"]', timeout=10000)
                await page.click(f'label[for="{request.is_active_lawsuit}"]')
                results.append(f"Clicked label for {request.is_active_lawsuit}")
            if request.is_forclosure is not None:
                await page.wait_for_selector(f'label[for="{request.is_forclosure}"]', timeout=10000)
                await page.click(f'label[for="{request.is_forclosure}"]')
                results.append(f"Clicked label for {request.is_forclosure}")
            if request.is_delinquent is not None:
                await page.wait_for_selector(f'label[for="{request.is_delinquent}"]', timeout=10000)
                await page.click(f'label[for="{request.is_delinquent}"]')
                results.append(f"Clicked label for {request.is_delinquent}")
            if request.is_fraud is not None:
                await page.wait_for_selector(f'label[for="{request.is_fraud}"]', timeout=10000)
                await page.click(f'label[for="{request.is_fraud}"]')
                results.append(f"Clicked label for {request.is_fraud}")
            if request.borrower_designated_beneficiary is not None:
                await page.wait_for_selector(f'label[for="{request.borrower_designated_beneficiary}"]', timeout=10000)
                await page.click(f'label[for="{request.borrower_designated_beneficiary}"]')
                results.append(f"Clicked label for {request.borrower_designated_beneficiary}")

            # After borrower_designated_beneficiary
            if request.flip_experience is not None:
                await page.wait_for_selector(f'label[for="{request.flip_experience}"]', timeout=10000)
                await page.click(f'label[for="{request.flip_experience}"]')
                results.append(f"Clicked label for {request.flip_experience}")
            if request.flips_completed is not None:
                await page.fill('#borNoOfREPropertiesCompleted', value=request.flips_completed)
                results.append(f"Filled #borNoOfREPropertiesCompleted with {request.flips_completed}")
            if request.ground_up_experience is not None:
                await page.wait_for_selector(f'label[for="{request.ground_up_experience}"]', timeout=10000)
                await page.click(f'label[for="{request.ground_up_experience}"]')
                results.append(f"Clicked label for {request.ground_up_experience}")
            if request.ground_ups_completed is not None:
                await page.fill('#borRehabPropCompleted', value=request.ground_ups_completed)
                results.append(f"Filled #borRehabPropCompleted with {request.ground_ups_completed}")
            if request.is_borrower_gc is not None:
                await page.wait_for_selector(f'label[for="{request.is_borrower_gc}"]', timeout=10000)
                await page.click(f'label[for="{request.is_borrower_gc}"]')
                results.append(f"Clicked label for {request.is_borrower_gc}")
            if request.rental_experience is not None:
                await page.wait_for_selector(f'label[for="{request.rental_experience}"]', timeout=10000)
                await page.click(f'label[for="{request.rental_experience}"]')
                results.append(f"Clicked label for {request.rental_experience}")
            if request.rentals_owned is not None:
                await page.fill('#borNoOfOwnProp', value=request.rentals_owned)
                results.append(f"Filled #borNoOfOwnProp with {request.rentals_owned}")
            if request.have_professional_licences is not None:
                await page.wait_for_selector(f'label[for="{request.have_professional_licences}"]', timeout=10000)
                await page.click(f'label[for="{request.have_professional_licences}"]')
                results.append(f"Clicked label for {request.have_professional_licences}")
            if request.professional_licences is not None:
                await page.select_option('#borProfLicence', value=request.professional_licences)
                results.append(f"Selected #borProfLicence with {request.professional_licences}")
            if request.liquid_assets is not None:
                await page.fill('#liquidAssets', value=request.liquid_assets)
                results.append(f"Filled #liquidAssets with {request.liquid_assets}")
            if request.desired_closing_date is not None:
                await page.fill('#desiredClosingDate', value=request.desired_closing_date)
                results.append(f"Filled #desiredClosingDate with {request.desired_closing_date}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after desired_closing_date")
            if request.desired_loan_amount is not None:
                await page.fill('#desiredLoanAmount', value=request.desired_loan_amount)
                results.append(f"Filled #desiredLoanAmount with {request.desired_loan_amount}")
            if request.type_of_loan_requesting is not None:
                await page.select_option('#typeOfHMLOLoanRequesting', value=request.type_of_loan_requesting)
                results.append(f"Selected #typeOfHMLOLoanRequesting with {request.type_of_loan_requesting}")
            if request.trial_payment_date is not None:
                await page.fill('#trialPaymentDate1', value=request.trial_payment_date)
                results.append(f"Filled #trialPaymentDate1 with {request.trial_payment_date}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after trial_payment_date")
            if request.maturity_date is not None:
                await page.fill('#maturityDate', value=request.maturity_date)
                results.append(f"Filled #maturityDate with {request.maturity_date}")
                await page.click('body', position={'x': 10, 'y': 10})
                results.append("Clicked body after maturity_date")
            if request.loan_term is not None:
                await page.select_option('#loanTerm', value=request.loan_term)
                results.append(f"Selected #loanTerm with {request.loan_term}")
            if request.interest_rate is not None:
                await page.wait_for_selector('input#lien1Rate', timeout=10000)
                await page.click('input#lien1Rate')
                await page.fill('input#lien1Rate', request.interest_rate)
                results.append(f"Filled #lien1Rate with {request.interest_rate}")
            if request.lien_terms is not None:
                await page.select_option('#lien1Terms', value=request.lien_terms)
                results.append(f"Selected #lien1Terms with {request.lien_terms}")
            if request.amortization_type is not None:
                await page.wait_for_selector(f'label[for="{request.amortization_type}"]', timeout=10000)
                await page.click(f'label[for="{request.amortization_type}"]')
                results.append(f"Clicked label for {request.amortization_type}")
            if request.is_taxes_ins_escrowed is not None:
                await page.wait_for_selector(f'label[for="{request.is_taxes_ins_escrowed}"]', timeout=10000)
                await page.click(f'label[for="{request.is_taxes_ins_escrowed}"]')
                results.append(f"Clicked label for {request.is_taxes_ins_escrowed}")
            if request.taxes is not None:
                await page.fill('#taxes1', value=request.taxes)
                results.append(f"Filled #taxes1 with {request.taxes}")
            if request.annual_premium is not None:
                await page.fill('#annualPremium', value=request.annual_premium)
                results.append(f"Filled #annualPremium with {request.annual_premium}")
            if request.cost_basis is not None:
                await page.fill('#costBasis', value=request.cost_basis)
                results.append(f"Filled #costBasis with {request.cost_basis}")
            if request.home_value is not None:
                await page.fill('#homeValue', value=request.home_value)
                results.append(f"Filled #homeValue with {request.home_value}")
            if request.max_amount_to_put_down is not None:
                await page.wait_for_selector('input#maxAmtToPutDown', timeout=10000)
                await page.click('input#maxAmtToPutDown')
                await page.fill('input#maxAmtToPutDown', request.max_amount_to_put_down)
                results.append(f"Filled #maxAmtToPutDown with {request.max_amount_to_put_down}")
            if request.subject_property_address is not None:
                await page.fill('#propertyAddress_1', value=request.subject_property_address)
                results.append(f"Filled #propertyAddress_1 with {request.subject_property_address}")
            if request.subject_property_unit is not None:
                await page.fill('#propertyUnit_1', value=request.subject_property_unit)
                results.append(f"Filled #propertyUnit_1 with {request.subject_property_unit}")
            if request.subject_property_city is not None:
                await page.fill('#propertyCity_1', value=request.subject_property_city)
                results.append(f"Filled #propertyCity_1 with {request.subject_property_city}")
            if request.subject_property_state is not None:
                await page.select_option('#propertyState_1', value=request.subject_property_state)
                results.append(f"Selected #propertyState_1 with {request.subject_property_state}")
            if request.subject_property_zip is not None:
                await page.fill('#propertyZip_1', value=request.subject_property_zip)
                results.append(f"Filled #propertyZip_1 with {request.subject_property_zip}")
            if request.subject_property_county is not None:
                await page.select_option('#propertyCounty_1', value=request.subject_property_county)
                results.append(f"Selected #propertyCounty_1 with {request.subject_property_county}")
            if request.subject_property_apn is not None:
                await page.fill('#parcelNo_1', value=request.subject_property_apn)
                results.append(f"Filled #parcelNo_1 with {request.subject_property_apn}")
            if request.subject_property_block is not None:
                await page.fill('#block_1', value=request.subject_property_block)
                results.append(f"Filled #block_1 with {request.subject_property_block}")
            if request.subject_property_lot is not None:
                await page.fill('#lot_1', value=request.subject_property_lot)
                results.append(f"Filled #lot_1 with {request.subject_property_lot}")
            if request.subject_property_type is not None and request.subject_property_type.strip() != "":
                await page.click('div#propertyType_chosen')
                await page.click(f'ul.chosen-results li:has-text("{request.subject_property_type}")')
                results.append(f"Selected property type {request.subject_property_type}")
            if request.subject_property_sqft is not None:
                await page.fill('#propertySqFt', value=request.subject_property_sqft)
                results.append(f"Filled #propertySqFt with {request.subject_property_sqft}")
            if request.subject_property_acres is not None:
                await page.fill('#acres', value=request.subject_property_acres)
                results.append(f"Filled #acres with {request.subject_property_acres}")
            if request.subject_property_year_built is not None:
                await page.fill('#yearBuilt', value=request.subject_property_year_built)
                results.append(f"Filled #yearBuilt with {request.subject_property_year_built}")
            if request.bedrooms is not None:
                await page.fill('#howManyBedRoom', value=request.bedrooms)
                results.append(f"Filled #howManyBedRoom with {request.bedrooms}")
            if request.bathrooms is not None:
                await page.fill('#howManyBathRoom', value=request.bathrooms)
                results.append(f"Filled #howManyBathRoom with {request.bathrooms}")
            if request.half_bathrooms is not None:
                await page.fill('#howManyHalfBathRoom', value=request.half_bathrooms)
                results.append(f"Filled #howManyHalfBathRoom with {request.half_bathrooms}")
            if request.number_of_buildings is not None:
                await page.fill('#noOfBuildings', value=request.number_of_buildings)
                results.append(f"Filled #noOfBuildings with {request.number_of_buildings}")
            if request.number_of_units_occupied is not None:
                await page.fill('#noUnitsOccupied', value=request.number_of_units_occupied)
                results.append(f"Filled #noUnitsOccupied with {request.number_of_units_occupied}")
            if request.number_of_parcels is not None:
                await page.fill('#noOfParcels', value=request.number_of_parcels)
                results.append(f"Filled #noOfParcels with {request.number_of_parcels}")
            if request.estimated_property_value is not None:
                await page.fill('#estimatedPropertyValue', value=request.estimated_property_value)
                results.append(f"Filled #estimatedPropertyValue with {request.estimated_property_value}")
            if request.present_occupancy is not None:
                await page.select_option('#presentOccupancy', value=request.present_occupancy)
                results.append(f"Selected #presentOccupancy with {request.present_occupancy}")

            # After present_occupancy
            if request.lb_contact_name is not None:
                await page.fill('#LBContactName', value=request.lb_contact_name)
                results.append(f"Filled #LBContactName with {request.lb_contact_name}")
            if request.lb_contact_email is not None:
                await page.fill('#LBContactEmail', value=request.lb_contact_email)
                results.append(f"Filled #LBContactEmail with {request.lb_contact_email}")
            if request.lb_contact_phone is not None:
                await page.fill('#LBContactPhone', value=request.lb_contact_phone)
                results.append(f"Filled #LBContactPhone with {request.lb_contact_phone}")
            if request.unit_type_1_1 is not None and request.unit_type_1_1.strip() != "":
                await page.click('div#unitType_1_1_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_1_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_1)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_1}")
            if request.unit_num_1_1 is not None:
                await page.fill('#unitNum_1_1', value=request.unit_num_1_1)
                results.append(f"Filled #unitNum_1_1 with {request.unit_num_1_1}")
            if request.sq_ft_1_1 is not None:
                await page.fill('#sqFt_1_1', value=request.sq_ft_1_1)
                results.append(f"Filled #sqFt_1_1 with {request.sq_ft_1_1}")
            if request.rent_roll_market_rents_1_1 is not None:
                await page.fill('#rentRollMarketRents_1_1', value=request.rent_roll_market_rents_1_1)
                results.append(f"Filled #rentRollMarketRents_1_1 with {request.rent_roll_market_rents_1_1}")
            if request.rent_roll_actual_rents_1_1 is not None:
                await page.fill('#rentRollActualRents_1_1', value=request.rent_roll_actual_rents_1_1)
                results.append(f"Filled #rentRollActualRents_1_1 with {request.rent_roll_actual_rents_1_1}")
            if request.rent_roll_monthly_rent_1_1 is not None:
                await page.fill('#rentRollMonthlyRent_1_1', value=request.rent_roll_monthly_rent_1_1)
                results.append(f"Filled #rentRollMonthlyRent_1_1 with {request.rent_roll_monthly_rent_1_1}")
            if request.rent_roll_vacant_no_1_1 is not None and request.rent_roll_vacant_no_1_1.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_1}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_1}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_1}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_2
            if request.unit_type_1_2 is not None and request.unit_type_1_2.strip() != "":
                await page.click('div#unitType_1_2_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_2_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_2)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_2} for entry 1_2")
            if request.unit_num_1_2 is not None and request.unit_num_1_2.strip() != "":
                await page.fill('#unitNum_1_2', value=request.unit_num_1_2)
                results.append(f"Filled #unitNum_1_2 with {request.unit_num_1_2}")
            if request.sq_ft_1_2 is not None and request.sq_ft_1_2.strip() != "":
                await page.fill('#sqFt_1_2', value=request.sq_ft_1_2)
                results.append(f"Filled #sqFt_1_2 with {request.sq_ft_1_2}")
            if request.rent_roll_market_rents_1_2 is not None and request.rent_roll_market_rents_1_2.strip() != "":
                await page.fill('#rentRollMarketRents_1_2', value=request.rent_roll_market_rents_1_2)
                results.append(f"Filled #rentRollMarketRents_1_2 with {request.rent_roll_market_rents_1_2}")
            if request.rent_roll_actual_rents_1_2 is not None and request.rent_roll_actual_rents_1_2.strip() != "":
                await page.fill('#rentRollActualRents_1_2', value=request.rent_roll_actual_rents_1_2)
                results.append(f"Filled #rentRollActualRents_1_2 with {request.rent_roll_actual_rents_1_2}")
            if request.rent_roll_monthly_rent_1_2 is not None and request.rent_roll_monthly_rent_1_2.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_2', value=request.rent_roll_monthly_rent_1_2)
                results.append(f"Filled #rentRollMonthlyRent_1_2 with {request.rent_roll_monthly_rent_1_2}")
            if request.rent_roll_vacant_no_1_2 is not None and request.rent_roll_vacant_no_1_2.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_2}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_2}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_2}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_3
            if request.unit_type_1_3 is not None and request.unit_type_1_3.strip() != "":
                await page.click('div#unitType_1_3_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_3_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_3)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_3} for entry 1_3")
            if request.unit_num_1_3 is not None and request.unit_num_1_3.strip() != "":
                await page.fill('#unitNum_1_3', value=request.unit_num_1_3)
                results.append(f"Filled #unitNum_1_3 with {request.unit_num_1_3}")
            if request.sq_ft_1_3 is not None and request.sq_ft_1_3.strip() != "":
                await page.fill('#sqFt_1_3', value=request.sq_ft_1_3)
                results.append(f"Filled #sqFt_1_3 with {request.sq_ft_1_3}")
            if request.rent_roll_market_rents_1_3 is not None and request.rent_roll_market_rents_1_3.strip() != "":
                await page.fill('#rentRollMarketRents_1_3', value=request.rent_roll_market_rents_1_3)
                results.append(f"Filled #rentRollMarketRents_1_3 with {request.rent_roll_market_rents_1_3}")
            if request.rent_roll_actual_rents_1_3 is not None and request.rent_roll_actual_rents_1_3.strip() != "":
                await page.fill('#rentRollActualRents_1_3', value=request.rent_roll_actual_rents_1_3)
                results.append(f"Filled #rentRollActualRents_1_3 with {request.rent_roll_actual_rents_1_3}")
            if request.rent_roll_monthly_rent_1_3 is not None and request.rent_roll_monthly_rent_1_3.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_3', value=request.rent_roll_monthly_rent_1_3)
                results.append(f"Filled #rentRollMonthlyRent_1_3 with {request.rent_roll_monthly_rent_1_3}")
            if request.rent_roll_vacant_no_1_3 is not None and request.rent_roll_vacant_no_1_3.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_3}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_3}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_3}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_4
            if request.unit_type_1_4 is not None and request.unit_type_1_4.strip() != "":
                await page.click('div#unitType_1_4_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_4_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_4)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_4} for entry 1_4")
            if request.unit_num_1_4 is not None and request.unit_num_1_4.strip() != "":
                await page.fill('#unitNum_1_4', value=request.unit_num_1_4)
                results.append(f"Filled #unitNum_1_4 with {request.unit_num_1_4}")
            if request.sq_ft_1_4 is not None and request.sq_ft_1_4.strip() != "":
                await page.fill('#sqFt_1_4', value=request.sq_ft_1_4)
                results.append(f"Filled #sqFt_1_4 with {request.sq_ft_1_4}")
            if request.rent_roll_market_rents_1_4 is not None and request.rent_roll_market_rents_1_4.strip() != "":
                await page.fill('#rentRollMarketRents_1_4', value=request.rent_roll_market_rents_1_4)
                results.append(f"Filled #rentRollMarketRents_1_4 with {request.rent_roll_market_rents_1_4}")
            if request.rent_roll_actual_rents_1_4 is not None and request.rent_roll_actual_rents_1_4.strip() != "":
                await page.fill('#rentRollActualRents_1_4', value=request.rent_roll_actual_rents_1_4)
                results.append(f"Filled #rentRollActualRents_1_4 with {request.rent_roll_actual_rents_1_4}")
            if request.rent_roll_monthly_rent_1_4 is not None and request.rent_roll_monthly_rent_1_4.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_4', value=request.rent_roll_monthly_rent_1_4)
                results.append(f"Filled #rentRollMonthlyRent_1_4 with {request.rent_roll_monthly_rent_1_4}")
            if request.rent_roll_vacant_no_1_4 is not None and request.rent_roll_vacant_no_1_4.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_4}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_4}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_4}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_5
            if request.unit_type_1_5 is not None and request.unit_type_1_5.strip() != "":
                await page.click('div#unitType_1_5_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_5_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_5)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_5} for entry 1_5")
            if request.unit_num_1_5 is not None and request.unit_num_1_5.strip() != "":
                await page.fill('#unitNum_1_5', value=request.unit_num_1_5)
                results.append(f"Filled #unitNum_1_5 with {request.unit_num_1_5}")
            if request.sq_ft_1_5 is not None and request.sq_ft_1_5.strip() != "":
                await page.fill('#sqFt_1_5', value=request.sq_ft_1_5)
                results.append(f"Filled #sqFt_1_5 with {request.sq_ft_1_5}")
            if request.rent_roll_market_rents_1_5 is not None and request.rent_roll_market_rents_1_5.strip() != "":
                await page.fill('#rentRollMarketRents_1_5', value=request.rent_roll_market_rents_1_5)
                results.append(f"Filled #rentRollMarketRents_1_5 with {request.rent_roll_market_rents_1_5}")
            if request.rent_roll_actual_rents_1_5 is not None and request.rent_roll_actual_rents_1_5.strip() != "":
                await page.fill('#rentRollActualRents_1_5', value=request.rent_roll_actual_rents_1_5)
                results.append(f"Filled #rentRollActualRents_1_5 with {request.rent_roll_actual_rents_1_5}")
            if request.rent_roll_monthly_rent_1_5 is not None and request.rent_roll_monthly_rent_1_5.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_5', value=request.rent_roll_monthly_rent_1_5)
                results.append(f"Filled #rentRollMonthlyRent_1_5 with {request.rent_roll_monthly_rent_1_5}")
            if request.rent_roll_vacant_no_1_5 is not None and request.rent_roll_vacant_no_1_5.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_5}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_5}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_5}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_6
            if request.unit_type_1_6 is not None and request.unit_type_1_6.strip() != "":
                await page.click('div#unitType_1_6_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_6_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_6)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_6} for entry 1_6")
            if request.unit_num_1_6 is not None and request.unit_num_1_6.strip() != "":
                await page.fill('#unitNum_1_6', value=request.unit_num_1_6)
                results.append(f"Filled #unitNum_1_6 with {request.unit_num_1_6}")
            if request.sq_ft_1_6 is not None and request.sq_ft_1_6.strip() != "":
                await page.fill('#sqFt_1_6', value=request.sq_ft_1_6)
                results.append(f"Filled #sqFt_1_6 with {request.sq_ft_1_6}")
            if request.rent_roll_market_rents_1_6 is not None and request.rent_roll_market_rents_1_6.strip() != "":
                await page.fill('#rentRollMarketRents_1_6', value=request.rent_roll_market_rents_1_6)
                results.append(f"Filled #rentRollMarketRents_1_6 with {request.rent_roll_market_rents_1_6}")
            if request.rent_roll_actual_rents_1_6 is not None and request.rent_roll_actual_rents_1_6.strip() != "":
                await page.fill('#rentRollActualRents_1_6', value=request.rent_roll_actual_rents_1_6)
                results.append(f"Filled #rentRollActualRents_1_6 with {request.rent_roll_actual_rents_1_6}")
            if request.rent_roll_monthly_rent_1_6 is not None and request.rent_roll_monthly_rent_1_6.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_6', value=request.rent_roll_monthly_rent_1_6)
                results.append(f"Filled #rentRollMonthlyRent_1_6 with {request.rent_roll_monthly_rent_1_6}")
            if request.rent_roll_vacant_no_1_6 is not None and request.rent_roll_vacant_no_1_6.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_6}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_6}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_6}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_7
            if request.unit_type_1_7 is not None and request.unit_type_1_7.strip() != "":
                await page.click('div#unitType_1_7_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_7_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_7)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_7} for entry 1_7")
            if request.unit_num_1_7 is not None and request.unit_num_1_7.strip() != "":
                await page.fill('#unitNum_1_7', value=request.unit_num_1_7)
                results.append(f"Filled #unitNum_1_7 with {request.unit_num_1_7}")
            if request.sq_ft_1_7 is not None and request.sq_ft_1_7.strip() != "":
                await page.fill('#sqFt_1_7', value=request.sq_ft_1_7)
                results.append(f"Filled #sqFt_1_7 with {request.sq_ft_1_7}")
            if request.rent_roll_market_rents_1_7 is not None and request.rent_roll_market_rents_1_7.strip() != "":
                await page.fill('#rentRollMarketRents_1_7', value=request.rent_roll_market_rents_1_7)
                results.append(f"Filled #rentRollMarketRents_1_7 with {request.rent_roll_market_rents_1_7}")
            if request.rent_roll_actual_rents_1_7 is not None and request.rent_roll_actual_rents_1_7.strip() != "":
                await page.fill('#rentRollActualRents_1_7', value=request.rent_roll_actual_rents_1_7)
                results.append(f"Filled #rentRollActualRents_1_7 with {request.rent_roll_actual_rents_1_7}")
            if request.rent_roll_monthly_rent_1_7 is not None and request.rent_roll_monthly_rent_1_7.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_7', value=request.rent_roll_monthly_rent_1_7)
                results.append(f"Filled #rentRollMonthlyRent_1_7 with {request.rent_roll_monthly_rent_1_7}")
            if request.rent_roll_vacant_no_1_7 is not None and request.rent_roll_vacant_no_1_7.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_7}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_7}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_7}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_8
            if request.unit_type_1_8 is not None and request.unit_type_1_8.strip() != "":
                await page.click('div#unitType_1_8_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_8_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_8)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_8} for entry 1_8")
            if request.unit_num_1_8 is not None and request.unit_num_1_8.strip() != "":
                await page.fill('#unitNum_1_8', value=request.unit_num_1_8)
                results.append(f"Filled #unitNum_1_8 with {request.unit_num_1_8}")
            if request.sq_ft_1_8 is not None and request.sq_ft_1_8.strip() != "":
                await page.fill('#sqFt_1_8', value=request.sq_ft_1_8)
                results.append(f"Filled #sqFt_1_8 with {request.sq_ft_1_8}")
            if request.rent_roll_market_rents_1_8 is not None and request.rent_roll_market_rents_1_8.strip() != "":
                await page.fill('#rentRollMarketRents_1_8', value=request.rent_roll_market_rents_1_8)
                results.append(f"Filled #rentRollMarketRents_1_8 with {request.rent_roll_market_rents_1_8}")
            if request.rent_roll_actual_rents_1_8 is not None and request.rent_roll_actual_rents_1_8.strip() != "":
                await page.fill('#rentRollActualRents_1_8', value=request.rent_roll_actual_rents_1_8)
                results.append(f"Filled #rentRollActualRents_1_8 with {request.rent_roll_actual_rents_1_8}")
            if request.rent_roll_monthly_rent_1_8 is not None and request.rent_roll_monthly_rent_1_8.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_8', value=request.rent_roll_monthly_rent_1_8)
                results.append(f"Filled #rentRollMonthlyRent_1_8 with {request.rent_roll_monthly_rent_1_8}")
            if request.rent_roll_vacant_no_1_8 is not None and request.rent_roll_vacant_no_1_8.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_8}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_8}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_8}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_9
            if request.unit_type_1_9 is not None and request.unit_type_1_9.strip() != "":
                await page.click('div#unitType_1_9_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_9_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_9)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_9} for entry 1_9")
            if request.unit_num_1_9 is not None and request.unit_num_1_9.strip() != "":
                await page.fill('#unitNum_1_9', value=request.unit_num_1_9)
                results.append(f"Filled #unitNum_1_9 with {request.unit_num_1_9}")
            if request.sq_ft_1_9 is not None and request.sq_ft_1_9.strip() != "":
                await page.fill('#sqFt_1_9', value=request.sq_ft_1_9)
                results.append(f"Filled #sqFt_1_9 with {request.sq_ft_1_9}")
            if request.rent_roll_market_rents_1_9 is not None and request.rent_roll_market_rents_1_9.strip() != "":
                await page.fill('#rentRollMarketRents_1_9', value=request.rent_roll_market_rents_1_9)
                results.append(f"Filled #rentRollMarketRents_1_9 with {request.rent_roll_market_rents_1_9}")
            if request.rent_roll_actual_rents_1_9 is not None and request.rent_roll_actual_rents_1_9.strip() != "":
                await page.fill('#rentRollActualRents_1_9', value=request.rent_roll_actual_rents_1_9)
                results.append(f"Filled #rentRollActualRents_1_9 with {request.rent_roll_actual_rents_1_9}")
            if request.rent_roll_monthly_rent_1_9 is not None and request.rent_roll_monthly_rent_1_9.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_9', value=request.rent_roll_monthly_rent_1_9)
                results.append(f"Filled #rentRollMonthlyRent_1_9 with {request.rent_roll_monthly_rent_1_9}")
            if request.rent_roll_vacant_no_1_9 is not None and request.rent_roll_vacant_no_1_9.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_9}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_9}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_9}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # Rent Roll Entry 1_10
            if request.unit_type_1_10 is not None and request.unit_type_1_10.strip() != "":
                await page.click('div#unitType_1_10_chosen')
                await page.wait_for_timeout(500)
                dropdown_option = page.locator(f'div#unitType_1_10_chosen + div ul.chosen-results li.active-result').filter(has_text=request.unit_type_1_10)
                await dropdown_option.wait_for(timeout=5000)
                await dropdown_option.click()
                results.append(f"Selected unit type {request.unit_type_1_10} for entry 1_10")
            if request.unit_num_1_10 is not None and request.unit_num_1_10.strip() != "":
                await page.fill('#unitNum_1_10', value=request.unit_num_1_10)
                results.append(f"Filled #unitNum_1_10 with {request.unit_num_1_10}")
            if request.sq_ft_1_10 is not None and request.sq_ft_1_10.strip() != "":
                await page.fill('#sqFt_1_10', value=request.sq_ft_1_10)
                results.append(f"Filled #sqFt_1_10 with {request.sq_ft_1_10}")
            if request.rent_roll_market_rents_1_10 is not None and request.rent_roll_market_rents_1_10.strip() != "":
                await page.fill('#rentRollMarketRents_1_10', value=request.rent_roll_market_rents_1_10)
                results.append(f"Filled #rentRollMarketRents_1_10 with {request.rent_roll_market_rents_1_10}")
            if request.rent_roll_actual_rents_1_10 is not None and request.rent_roll_actual_rents_1_10.strip() != "":
                await page.fill('#rentRollActualRents_1_10', value=request.rent_roll_actual_rents_1_10)
                results.append(f"Filled #rentRollActualRents_1_10 with {request.rent_roll_actual_rents_1_10}")
            if request.rent_roll_monthly_rent_1_10 is not None and request.rent_roll_monthly_rent_1_10.strip() != "":
                await page.fill('#rentRollMonthlyRent_1_10', value=request.rent_roll_monthly_rent_1_10)
                results.append(f"Filled #rentRollMonthlyRent_1_10 with {request.rent_roll_monthly_rent_1_10}")
            if request.rent_roll_vacant_no_1_10 is not None and request.rent_roll_vacant_no_1_10.strip() != "":
                await page.wait_for_selector(f'label[for="{request.rent_roll_vacant_no_1_10}"]', timeout=10000)
                await page.click(f'label[for="{request.rent_roll_vacant_no_1_10}"]')
                results.append(f"Clicked label for {request.rent_roll_vacant_no_1_10}")
            await page.click('//span[contains(@class, "autosavePropertyRentRoll") and contains(@onclick, "cloneFormSection")]')
            results.append("Clicked plus icon to add more rent roll entries")
            await page.wait_for_timeout(1000)
            results.append("Waited 1s for new rent roll form to render")

            # HOA and Occupancy Information
            if request.is_hoa_available_yes_1_is_hoa_available is not None and request.is_hoa_available_yes_1_is_hoa_available.strip() != "":
                await page.wait_for_selector(f'label[for="{request.is_hoa_available_yes_1_is_hoa_available}"]', timeout=10000)
                await page.click(f'label[for="{request.is_hoa_available_yes_1_is_hoa_available}"]')
                results.append(f"Clicked label for {request.is_hoa_available_yes_1_is_hoa_available}")
            if request.monthly_hoa_fees is not None and request.monthly_hoa_fees.strip() != "":
                await page.fill('#monthlyHOAFees', value=request.monthly_hoa_fees)
                results.append(f"Filled #monthlyHOAFees with {request.monthly_hoa_fees}")
            if request.actual_rents_in_place is not None and request.actual_rents_in_place.strip() != "":
                await page.wait_for_selector('input#actualRentsInPlace', timeout=10000)
                await page.click('input#actualRentsInPlace')
                await page.fill('input#actualRentsInPlace', request.actual_rents_in_place)
                results.append(f"Filled #actualRentsInPlace with {request.actual_rents_in_place}")
            if request.spcf_hoafees is not None and request.spcf_hoafees.strip() != "":
                await page.wait_for_selector('input#spcf_hoafees', timeout=10000)
                await page.click('input#spcf_hoafees')
                await page.fill('input#spcf_hoafees', request.spcf_hoafees)
                results.append(f"Filled #spcf_hoafees with {request.spcf_hoafees}")
            if request.is_bor_intend_to_occupy_prop_as_pri_no is not None and request.is_bor_intend_to_occupy_prop_as_pri_no.strip() != "":
                await page.wait_for_selector(f'label[for="{request.is_bor_intend_to_occupy_prop_as_pri_no}"]', timeout=10000)
                await page.click(f'label[for="{request.is_bor_intend_to_occupy_prop_as_pri_no}"]')
                results.append(f"Clicked label for {request.is_bor_intend_to_occupy_prop_as_pri_no}")
            if request.is_co_bor_intend_to_occupy_prop_as_pri_no is not None and request.is_co_bor_intend_to_occupy_prop_as_pri_no.strip() != "":
                await page.wait_for_selector(f'label[for="{request.is_co_bor_intend_to_occupy_prop_as_pri_no}"]', timeout=10000)
                await page.click(f'label[for="{request.is_co_bor_intend_to_occupy_prop_as_pri_no}"]')
                results.append(f"Clicked label for {request.is_co_bor_intend_to_occupy_prop_as_pri_no}")

            # Title Information
            if request.title_seller is not None and request.title_seller.strip() != "":
                await page.fill('#titleSeller', value=request.title_seller)
                results.append(f"Filled #titleSeller with {request.title_seller}")
            if request.title_name is not None and request.title_name.strip() != "":
                await page.fill('#titleName', value=request.title_name)
                results.append(f"Filled #titleName with {request.title_name}")
            if request.title_order_number is not None and request.title_order_number.strip() != "":
                await page.fill('#titleOrderNumber', value=request.title_order_number)
                results.append(f"Filled #titleOrderNumber with {request.title_order_number}")

            # Property Insurance Information
            if request.pro_ins_first_name_1 is not None and request.pro_ins_first_name_1.strip() != "":
                await page.fill('#proInsFirstName_1', value=request.pro_ins_first_name_1)
                results.append(f"Filled #proInsFirstName_1 with {request.pro_ins_first_name_1}")
            if request.pro_ins_last_name_1 is not None and request.pro_ins_last_name_1.strip() != "":
                await page.fill('#proInsLastName_1', value=request.pro_ins_last_name_1)
                results.append(f"Filled #proInsLastName_1 with {request.pro_ins_last_name_1}")
            if request.pro_ins_name_1 is not None and request.pro_ins_name_1.strip() != "":
                await page.fill('#proInsName_1', value=request.pro_ins_name_1)
                results.append(f"Filled #proInsName_1 with {request.pro_ins_name_1}")
            if request.pro_inc_email_1 is not None and request.pro_inc_email_1.strip() != "":
                await page.fill('#proIncEmail_1', value=request.pro_inc_email_1)
                results.append(f"Filled #proIncEmail_1 with {request.pro_inc_email_1}")
            if request.pro_inc_ph_1 is not None and request.pro_inc_ph_1.strip() != "":
                await page.fill('#proIncPh_1', value=request.pro_inc_ph_1)
                results.append(f"Filled #proIncPh_1 with {request.pro_inc_ph_1}")

            await browser.close()
    except Exception as e:
        results.append(f"Error during automation: {str(e)}")
        # Attempt to close browser if it was opened
        try:
            if 'browser' in locals() and browser:
                await browser.close()
        except Exception:
            pass
    return results

@app.post("/run-actions")
async def run_actions(request: ActionRequest):
    try:
        results = await run_playwright_actions(request)
        return {"status": "success", "actions": results}
    except Exception as e:
        return {"status": "error", "message": str(e), "actions": []} 