import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

w70 = pd.read_csv('/Users/ahaynes/pflotran_work/elkhorn_slough/data/water_levels/W70_adjusted/final_WL_adjusted.csv')
p70 = pd.read_csv('/Users/ahaynes/pflotran_work/elkhorn_slough/data/water_levels/P70_adjusted/P70_adjusted.csv')
et = pd.read_csv('/Users/ahaynes/pflotran_work/elkhorn_slough/data/ET/evapo_CIMIS_WY2021_vol_edited_csv.csv')
precip = pd.read_csv('/Users/ahaynes/pflotran_work/elkhorn_slough/data/water_levels/raw/precip_wy21_.csv')
# print(w70)
# mid_w70 = w70[['datetime','mid_marsh_adjusted']]
# low_w70 = w70[['datetime','lower_marsh_adjusted']]
# upp_w70 = w70[['datetime','upper_marsh_adjusted']]
# w70['lower_marsh_adjusted'] = w70['lower_marsh_adjusted']/10*1.705
# w70['mid_marsh_adjusted'] = w70['mid_marsh_adjusted']/10*1.705
# w70['upper_marsh_adjusted'] = w70['upper_marsh_adjusted']/10*1.705
# p70['n2'] = p70['n2']/10*1.705
# p70['n3'] = p70['n3']/10*1.705
# p70['n1'] = p70['n1']/10*1.705
# # w70 = w70.set_index('datetime')

plt.rcParams['font.family'] = 'Futura'
plt.rcParams.update({'font.size': 20})
# fig, ax = plt.subplots(figsize=(10, 6))  # Increase figure size for better resolution
# # p70.plot(x= 'time_s', y='n3', ax=ax, label='Upper-marsh observed', color='C6')  # Set color to distinguish lines
# # merged_df.plot(x= 'datetime', y='mid_marsh_adjusted', ax=ax, label='Modeled data', color='C1')
# p70.plot(x= 'time_s', y='n1', ax=ax, label='Lower-marsh observed', color='C9')
# # p70.plot(x= 'time_s', y='n2', ax=ax, label='Mid-marsh observed p70', color='C4')
# ax.set_title ('Lower-marsh boundary conditions')
# ax.set_ylabel('Water level (m)')  # Add units to axis label
# ax.set_xlabel('Time (s)')  # Add x-axis label
# ax.set_ylim(1, 2)  # Zoom in on y-axis to highlight variation
# ax.axhline(y=1.59, color='r', linestyle='--', label = 'Marsh elevation (MASL)')
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
# ax.xaxis.set_tick_params(rotation=45)  # Rotate x-axis tick labels for better readability
# ax.tick_params(axis='both', which='major', labelsize=16)  # Increase tick label size

# ax.legend(loc='lower right', fontsize=14)  # Increase legend font size

# plt.tight_layout()  # Adjust spacing for better layout
# plt.show()
# Merge the data on the 'date' column
merged_df = pd.merge(et, precip, on='date', how='outer')

# Set the date range as the index of the merged dataframe
date_range = pd.date_range(start='2020-10-01', end='2021-09-30', freq='D')
merged_df = merged_df.set_index(date_range)

# Create a figure with two y-axes
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Plot precipitation on the first y-axis
ax1.bar(merged_df.index, merged_df['daily_y'], color='blue', label='Precipitation')
ax1.set_ylabel('Precipitation (mm/day)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Plot evapotranspiration on the second y-axis
ax2.bar(merged_df.index, merged_df['daily_x'], color='red', label='Evapotranspiration')
ax2.set_ylabel('Evapotranspiration (m^3/day)', color='red')
# ax2.set_ylim(-80, 0)
ax2.tick_params(axis='y', labelcolor='red')

# Set the x-axis label and ticks
ax1.set_xlabel('Date')
# ax1.xaxis.set_major_locator(mdates.MonthLocator())
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax1.xaxis.set_tick_params(rotation=45)  # Rotate x-axis tick labels for better readability , alpha=0.5, width=0.5

# Add legend and adjust layout
# Combine the legends from both axes

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
ax1.legend(handles, labels, loc='lower right', fontsize = 14)
  # Increase legend font size
# Add a title to the figure
fig.suptitle('Precipitation and ET WY21')
plt.tight_layout()
plt.show()