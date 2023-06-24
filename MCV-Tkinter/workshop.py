self.down_scope_label = ttk.Label(tab0, text='górny zakres:')
self.down_scope_label.grid(row=3, column=0)

self.down_scope_var = tk.StringVar()
self.down_scope_entry = ttk.Entry(tab0, textvariable=self.down_scope_var, width=30)
self.down_scope_entry.grid(row=3, column=1, sticky=tk.NSEW)