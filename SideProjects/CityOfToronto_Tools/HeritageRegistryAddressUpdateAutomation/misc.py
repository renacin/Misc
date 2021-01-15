

# This Function Will Clean Our & Keep Consistency Between Our Dataframes
def clean_df(data_frame, list_of_fieldnames):

    # -----------------------------------------------------------------------------------------------------------------
    # This Function Will Concatinate String If Longer Than Expected
    def concat_string(detail):
        text_len = 250
    	if len(detail) > text_len:
    		return detail[0:text_len]
    	else:
    		return detail

    # This Function Will Clean Not A Number Occurences | Nested Function As Not Needed Anywhere Else
    def remove_nan_space(d_frame, list_of_fieldnames):

        # Correct Nan Values That Might Be Present
        d_frame.fillna("", inplace=True)
        d_frame.replace(" ", "", inplace=True)   # Redo Just In Case After?
        d_frame.replace("nan", "", inplace=True)
        d_frame.replace("None", "", inplace=True)

        # Strip Whitespace Before Concatination
        for column in list_of_fieldnames[3:]:
        	d_frame[column] = d_frame[column].str.strip()

        return d_frame

    # ------------------------------------------------------------------------------------------------------------------
    # Covert Certain Fields To String
    for column in list_of_fieldnames[3:]:
    	data_frame[column] = data_frame[column].astype(str)

    # Clean Dataframe Before Concatination
    data_frame = remove_nan_space(data_frame, list_of_fieldnames)

    # Concat Stored Text To A Common Lenght: ArcGIS Text Is Max 250 Characters Long
    details_list = data_frame["Details"].tolist()
    data_frame["Details"] = [concat_string(x) for x in details_list]

    # Clean Dataframe Before Concatination
    data_frame = remove_nan_space(data_frame, list_of_fieldnames)

    return data_frame
