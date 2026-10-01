# Integration capability matrix

Read this reference before designing external execution. It records verified capability as of **2026-09-10**, not permanent truth. Re-check official documentation before relying on any capability, plan tier, endpoint, permission, or platform rule.

| System | Confirmed path | Important boundary | Safe fallback |
|---|---|---|---|
| Metricool | MCP is described as available across plans; REST API can export metrics and automate scheduling/publishing; official example uses `POST /v2/scheduler/posts`. | Direct API access is documented for Advanced/Custom plans. Tokens, `userId`, and `blogId` are required; keep the token server-side. Connected networks have platform-specific limits. | Use the connected MCP/tool if present; otherwise produce an import-ready calendar and request the user to schedule it. |
| Amazon KDP | KDP Reports provides downloadable orders, royalties, KENP, preorders, and payment reports with different refresh/finality rules. | Do not assume a public KDP management API. Orders, estimated royalties, finalized royalties, and payments are not interchangeable. Publishing, price, metadata, and exclusivity changes require approval. | Ask for/export the official report and analyze the file; use browser assistance only with authorization and confirmation. |
| Amazon Ads | Amazon Ads API supports programmatic campaign management and reporting for approved applicants and products. | API use requires registration/approval and account authorization. Amazon DSP availability does not prove access to every sponsored-ads operation. | Produce campaign settings/import sheets or guide manual execution; analyze exported reports. |
| Goodreads | Goodreads states it has not issued new public developer keys since 2020 and planned retirement of the public API. | Do not design a new system around a presumed Goodreads API. Avoid unauthorized scraping and automated review activity. | Use user-provided exports, permitted public research, or manual/approved browser workflows. |
| BookBub | Partners surfaces support Ads, Featured Deals, Preorders/Featured New Releases, and author-facing promotion workflows. | Availability and acceptance vary; do not claim placement or an automation API without current proof. | Prepare targeting, creative, submission data, and an approval checklist for manual execution. |
| Canva, Gmail, WordPress, ad/social connectors | Capabilities depend on installed plugins, connected accounts, scopes, plan, and the current tool schema. | Never infer that a named plugin is installed or authorized. Sending, publishing, and editing external state remain subject to the action envelope. | Generate source assets, email drafts, page copy, or structured payloads locally.

## Official sources

- Metricool API access: https://help.metricool.com/api-access-export-your-metricool-data-to-other-tools-and-automate-tasks-x8ln5
- Metricool API integration: https://help.metricool.com/basic-guide-for-api-integration-r97af
- Metricool scheduler endpoint example: https://help.metricool.com/wli-scheduler-endpoint-example-on-a-custom-backend-proxy-frko7
- KDP Reports: https://kdp.amazon.com/en_US/help/topic/GVTTXHKHVPAPBEDQ/
- KDP Sales and Royalties report: https://kdp.amazon.com/en_US/help/topic/G201488550/
- Amazon Ads API: https://advertising.amazon.com/en-ca/about-api
- Goodreads Developers group/API notice: https://www.goodreads.com/group/show/8095-goodreads-developers
- BookBub Partners: https://partners.bookbub.com/

## Capability check before execution

1. Inspect currently available tools rather than trusting the project brief.
2. Verify the target account, scope, plan, and permission.
3. Read the current tool schema or official endpoint documentation.
4. Test read-only access first when practical.
5. Preview the exact mutation and classify its approval level.
6. After execution, capture the external confirmation or ID; never infer success from a submitted request alone.
