---
layout: content
heading: Analysing multiple datasets
subheading: "Option 3: Federated analysis"
transition: slide-up
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <ApproachDiagram kind="federated" />
  </div>
  <div style="flex: 1;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Strategy:</strong> Send analysis code to the data; only aggregate results return</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Pros:</strong> Data never leaves its location; owners keep control and access rights</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Cons:</strong>
        <ul style="padding-left: 1.5rem; margin: 0.3rem 0 0 0;">
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Needs common infrastructure</li>
          <li style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Fewer analysis options than pooling</li>
        </ul>
      </li>
    </ul>
  </div>
</div>
