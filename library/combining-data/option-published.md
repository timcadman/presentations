---
layout: content
heading: Analysing multiple datasets
subheading: "Option 4: Publish summary data"
transition: slide-up
clicks: 2
---

<div style="display: flex; gap: 2rem; align-items: flex-start;">
  <div style="flex: 1; display: flex; align-items: center; justify-content: center;">
  <ApproachDiagram kind="published" />
  </div>
  <div style="flex: 1;">
    <ul style="padding-left: 1.5rem; margin: 0;">
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Strategy:</strong> Curate and publish summary statistics from each study</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Pros:</strong> No data sharing; anyone can reuse results</li>
      <li style="font-size: 18px; margin-bottom: 0.5rem; line-height: 1.5;"><strong>Cons:</strong>
        <ul style="padding-left: 1.5rem; margin: 0.3rem 0 0 0;">
          <li v-click="1" style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Limited to the published statistics, e.g. no mixed models across sites</li>
          <li v-click="2" style="font-size: 18px; margin-bottom: 0.3rem; line-height: 1.5;">Cannot choose your own effect modifiers</li>
        </ul>
      </li>
    </ul>
  </div>
</div>
